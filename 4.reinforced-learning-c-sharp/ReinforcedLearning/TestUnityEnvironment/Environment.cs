using System.Collections.Generic;
using ReinforcedLearning.Interfaces;

namespace TestUnityEnvironment
{
    public class Environment : IEnvApi
    {
        private readonly IAiSystemApi _api;
        private readonly CarScoreController _scoreController = new CarScoreController();
        
        public MovementVector MovementVector;
        
        public Environment(IAiSystemApi api)
        {
            _api = api;
            _api.Initialize(this);
        }
        
        public float[] GetInitialDistances() => _scoreController.GetInitialRaycasts().Distances;

        public void TakeSimulationStep() // CarAiDecisionGetter
        {
            var score = _scoreController.GetScore();
            
            // SendStateGetAction() {
            var rotation = _api.Predict(score);
            // SendStateGetAction() }

            MovementVector = new MovementVector() { Forward = 1, Rotation = rotation };
        }
    }
}