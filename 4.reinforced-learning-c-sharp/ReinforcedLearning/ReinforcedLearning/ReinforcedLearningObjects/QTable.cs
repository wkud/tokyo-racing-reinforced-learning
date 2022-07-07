using System;
using System.Collections.Generic;
using System.Collections.Immutable;

namespace ReinforcedLearning.ReinforcedLearningObjects
{
    
    
    public class QTable
    {
        /// <summary>
        /// the higher precision, the less often RL algorithm will
        /// encounter that value and learn from it's instance
        /// (highest rounding precision means every value is unique)
        /// </summary>
        private const int STATE_FLOAT_ROUNDING_PRECISION = 2;
        
        private struct QTableKey
        {
            // fields for hash code, don't delete
            private ImmutableArray<float> _stateKey;
            private int _actionKey;

            public QTableKey(State state, Action action)
            {
                _stateKey = state.ToImmutable(QTable.STATE_FLOAT_ROUNDING_PRECISION);
                _actionKey = action.Id;
            }
        }
        
        private readonly Dictionary<QTableKey, float> _qTable = new(); 

        public float Get(State state, Action action)
        {
            var key = new QTableKey(state, action);
            return _qTable.ContainsKey(key) ? _qTable[key] : 0;
        }
        
        public void Set(State state, Action action, float newQValue)
        {
            var key = new QTableKey(state, action);
            var success = _qTable.TryAdd(key, newQValue);
            if (!success)
            {
                _qTable[key] = newQValue;
            }
        }
    }
}