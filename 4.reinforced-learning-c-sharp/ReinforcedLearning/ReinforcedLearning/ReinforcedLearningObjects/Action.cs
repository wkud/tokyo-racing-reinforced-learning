using System;
using System.Collections.Generic;
using System.Linq;

namespace ReinforcedLearning.ReinforcedLearningObjects
{
    public class Action
    {
        public int Id { get; set; }
        public float Rotation { get; set; }

        private Action(int id, float rotation)
        {
            Id = id;
            Rotation = rotation;
        }

        public static Action Left = new Action(0, -1);
        public static Action Straight = new Action(1, 0);
        public static Action Right = new Action(2, 1);

        private static List<Action> _availableActions = new List<Action>() { Left, Straight, Right };

        public static List<Action> GetAvailableActions(State state)
        {
            return _availableActions; // can depend on state
        }

        public static Action FromRotation(float rotation)
        {
            return _availableActions.FirstOrDefault(a => Math.Abs(a.Rotation - rotation) <= 0);
        }
    }
}