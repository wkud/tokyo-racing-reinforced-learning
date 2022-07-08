using System;

namespace ReinforcedLearning.Interfaces
{
    public interface IAiSystemApi
    {
        float Predict(IFrameData frameData);
        void Initialize(IEnvApi envApi);
        void PrintQTable(Action<string> printCallback);
    }
}