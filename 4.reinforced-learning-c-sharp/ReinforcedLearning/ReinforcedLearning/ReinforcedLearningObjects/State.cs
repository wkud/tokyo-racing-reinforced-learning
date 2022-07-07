using System;
using System.Collections.Immutable;
using System.Linq;

namespace ReinforcedLearning.ReinforcedLearningObjects
{
    public class State
    {
        private float[] Distances { get; }

        public State(float[] distances)
        {
            Distances = distances;
        }

        public static State GetInitialState()
        {
            return new State(new float[] { 0, 0, 0, 0, 0, 0, 0, 0, 0 });
        }

        public ImmutableArray<float> ToImmutable(int roundingDigits)
        {
            var immutable = Distances
                .Select(e => MathF.Round(e, roundingDigits))
                .ToList()
                .ToImmutableArray();
            return immutable;
        }
    }
}