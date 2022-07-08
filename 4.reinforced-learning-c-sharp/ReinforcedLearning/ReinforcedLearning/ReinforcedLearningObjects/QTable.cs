using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;

namespace ReinforcedLearning.ReinforcedLearningObjects
{
    public class QTable
    {
        /// <summary>
        /// the higher precision, the less often RL algorithm will
        /// encounter that value and learn from it's instance
        /// (highest rounding precision means every value is unique)
        /// </summary>
        private const int STATE_FLOAT_ROUNDING_PRECISION = 0;
        
        private struct QTableKey
        {
            // fields for hash code, don't delete
            public ImmutableArray<float> StateKey { get; }
            public int ActionKey { get; }

            public QTableKey(State state, Action action)
            {
                StateKey = state.ToImmutable(QTable.STATE_FLOAT_ROUNDING_PRECISION);
                ActionKey = action.Id;
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

        public void Print(Action<string> printCallback)
        {
            var filteredKeys = _qTable.Keys.Where(k => _qTable[k] != 0).ToArray();

            var leftKeys = filteredKeys.Where(k => k.ActionKey == Action.Left.Id);
            var straightKeys = filteredKeys.Where(k => k.ActionKey == Action.Straight.Id);
            var rightKeys = filteredKeys.Where(k => k.ActionKey == Action.Right.Id);

            printCallback("Left");
            foreach (var key in leftKeys)
            {
                printCallback($"{key.StateKey} -> Left => Q={_qTable[key]}");
            }
            
            printCallback("Straight");
            foreach (var key in straightKeys)
            {
                printCallback($"{key.StateKey} -> Straight => Q={_qTable[key]}");
            }
            
            printCallback("Right");
            foreach (var key in rightKeys)
            {
                printCallback($"{key.StateKey} -> Right => Q={_qTable[key]}");
            }
        }
    }
}