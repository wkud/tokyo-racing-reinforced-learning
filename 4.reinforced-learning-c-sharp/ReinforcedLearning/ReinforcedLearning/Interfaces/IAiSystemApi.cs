namespace ReinforcedLearning.Interfaces
{
    public interface IAiSystemApi
    {
        float Predict(IFrameData frameData);
        void Initialize();
    }
}