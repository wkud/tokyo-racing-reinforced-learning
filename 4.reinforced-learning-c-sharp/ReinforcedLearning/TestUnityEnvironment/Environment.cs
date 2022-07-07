using System.Collections.Generic;
using ReinforcedLearning.Interfaces;
using TestUnityEnvironment.Data;

namespace TestUnityEnvironment
{
    public class Environment
    {
        private IAiSystemApi _api;

        public MovementVector MovementVector;
        
        public Environment(IAiSystemApi api)
        {
            _api = api;
            _api.Initialize();
        }

        private FrameData GetScore() // CarScoreController
        {
            return FrameData.GenerateRandom();
        }
        
        public void TakeSimulationStep() // CarAiDecisionGetter
        {
            var score = GetScore();
            
            // SendStateGetAction() {
            var rotation = _api.Predict(score);
            // SendStateGetAction() }

            MovementVector = new MovementVector() { Forward = 1, Rotation = rotation };
        }
    }
}