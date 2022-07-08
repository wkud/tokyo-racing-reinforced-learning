using TestUnityEnvironment.Data;

namespace TestUnityEnvironment
{
    internal class CarScoreController
    {
        public RaycastData GetInitialRaycasts() // CarScoreController
        {
            return new RaycastData() { Distances = new float[] { 0, 0, 0, 0, 0, 0, 0, 0, 0 } };
        }

        public FrameData GetScore() // CarScoreController
        {
            return FrameData.GenerateRandom();
        }
    }
}