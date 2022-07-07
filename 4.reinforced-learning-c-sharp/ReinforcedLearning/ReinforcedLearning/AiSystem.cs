using System.Collections.Generic;
using ReinforcedLearning.Dtos;
using ReinforcedLearning.Interfaces;
using ReinforcedLearning.ReinforcedLearningObjects;

namespace ReinforcedLearning
{
    public class AiSystem : IAiSystemApi
    {
        private readonly float _alphaLearningRate;
        private readonly float _gammaDiscountRate;

        private State _state;
        private Action _action;
        private readonly QTable _q;
        private readonly Policy _policy;
        
        public AiSystem(float alphaLearningRate, float epsilonProbabilityOfBest, float gammaDiscountRate)
        {
            _q = new QTable();
            _alphaLearningRate = alphaLearningRate;
            _policy = new Policy(epsilonProbabilityOfBest, Action.GetAvailableActions, _q.Get);
            _gammaDiscountRate = gammaDiscountRate;
        }

        public void Initialize()
        {
            _state = State.GetInitialState();
            _action = _policy.ChooseAction(_state);
        }

        public float Predict(IFrameData frameData) => PredictAndLearn(FrameDataDto.FromFrameData(frameData));

        private float PredictAndLearn(FrameDataDto dto)
        {
            var newAction = _policy.ChooseAction(dto.NewState);
            
            var newQ = _q.Get(_state, _action) + _alphaLearningRate *
                (dto.Reward + _gammaDiscountRate * _q.Get(dto.NewState, newAction) - _q.Get(_state, _action));
            _q.Set(_state, _action, newQ);

            _state = dto.NewState;
            _action = newAction;

            return newAction.Rotation;
        }
    }

    
}