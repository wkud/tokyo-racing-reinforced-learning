using ReinforcedLearning.Interfaces;
using ReinforcedLearning.ReinforcedLearningObjects;

namespace ReinforcedLearning.Dtos
{
    public class FrameDataDto
    {
        public float Reward { get; private init; }
        public bool IsTerminalState { get; private init; }
        public Action TakenAction { get; private init; }
        public State NewState { get; private init; }

        public static FrameDataDto FromFrameData(IFrameData frameData)
        {
            return new FrameDataDto()
            {
                Reward = frameData.Reward,
                IsTerminalState = frameData.IsTerminalState,
                TakenAction = Action.FromRotation(frameData.Rotation),
                NewState = new State(frameData.Distances),
            };
        }
    }
}