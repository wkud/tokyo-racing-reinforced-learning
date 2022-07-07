using System;
using System.Collections.Generic;
using System.Linq;

namespace ReinforcedLearning.ReinforcedLearningObjects
{
    public class Policy
    {
        private readonly float _epsilonProbabilityOfBest;
        private readonly Func<State, List<Action>> _getAvailableActionsCallback;
        private readonly Func<State, Action, float> _getQCallback;

        public Policy(float epsilonProbabilityOfBest, Func<State, List<Action>> getAvailableActionsCallback,
            Func<State, Action, float> getQCallback)
        {
            _epsilonProbabilityOfBest = epsilonProbabilityOfBest;
            _getAvailableActionsCallback = getAvailableActionsCallback;
            _getQCallback = getQCallback;
        }

        public Action ChooseAction(State state)
        {
            var availableActions = _getAvailableActionsCallback(state);

            var p = new Random().NextDouble();
            if (p < _epsilonProbabilityOfBest)
            {
                var qValuesOfActions = availableActions.Select(a => _getQCallback(state, a));
                var valuesOfActions = qValuesOfActions.ToList();

                var maxQValue = valuesOfActions.Max();
                var maxIndex = valuesOfActions.IndexOf(maxQValue);
                return availableActions[maxIndex];
            }
            else
            {
                var randomIndex = new Random().Next(availableActions.Count);
                return availableActions[randomIndex];
            }
        }
    }
}