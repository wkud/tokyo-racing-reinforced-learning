namespace ReinforcedLearning.Interfaces
{
    public interface IFrameData
    {
        public float Reward { get; }
        public bool IsTerminalState { get; }
        public float Rotation { get; }
        public float[] Distances { get; }
    }
}