using System;
using System.Collections.Generic;
using ReinforcedLearning.Interfaces;

namespace TestUnityEnvironment.Data
{
    [Serializable]
    public class FrameData : IFrameData //: ICsvSerializable
    {
        public ScoreData Score;
        public MovementVector Input;
        public RaycastData Raycasts;
        public bool IsGameOver;

        public float Reward => Score.ScoreForEqualLeftRightDistance;
        public bool IsTerminalState => IsGameOver;
        public float Rotation => Input.Rotation;
        public float[] Distances => Raycasts.Distances;


        public static FrameData GenerateRandom()
        {
            var r = new Random().Next(_frameDataValues.Count);
            return _frameDataValues[r];
        }
        

        private static List<FrameData> _frameDataValues = new List<FrameData>()
        {
            new FrameData()
            {
                Score = new ScoreData() { ScoreForEqualLeftRightDistance = 100 },
                IsGameOver = false,
                Input = new MovementVector() { Rotation = 0 },
                Raycasts = new RaycastData()
                {
                    Distances = new float[] { 3.655f, 3.9896f, 5.2739f, 10.067f, 17.701f, 10.0675f, 5.2739f, 3.9896f, 3.655f }
                },
            },
            new FrameData()
            {
                Score = new ScoreData() { ScoreForEqualLeftRightDistance = 10 },
                IsGameOver = false,
                Input = new MovementVector() { Rotation = 0 },
                Raycasts = new RaycastData()
                {
                    Distances = new float[] { 3.655f, 3.9896f, 5.2739f, 9.58f, 13.4201f, 21.9183f, 5.2739f, 3.9896f, 3.655f }
                },
            },
            new FrameData()
            {
                Score = new ScoreData() { ScoreForEqualLeftRightDistance = -100 },
                IsGameOver = false,
                Input = new MovementVector() { Rotation = 0 },
                Raycasts = new RaycastData()
                {
                    Distances = new float[] { 3.655f, 3.9896f, 5.2739f, 6.9803f, 9.1701f, 18.572f, 5.2739f, 3.9896f, 3.655f }
                },
            },
            new FrameData()
            {
                Score = new ScoreData() { ScoreForEqualLeftRightDistance = 50 },
                IsGameOver = false,
                Input = new MovementVector() { Rotation = 0 },
                Raycasts = new RaycastData()
                {
                    Distances = new float[] { 3.655f, 3.5891f, 3.5947f, 3.9777f, 5.1701f, 15.1641f, 13.5955f, 5.6574f, 3.655f }
                },
            },
            new FrameData()
            {
                Score = new ScoreData() { ScoreForEqualLeftRightDistance = -20 },
                IsGameOver = false,
                Input = new MovementVector() { Rotation = 0 },
                Raycasts = new RaycastData()
                {
                    Distances = new float[] { 1.3552f, 0.9298f, 0.7628f, 0.8277f, 1.1701f, 2.4177f, 11.5825f, 10.4676f, 7.0902f }
                },
            },
        };

        // public string GetCsvData() 
        // {
        //     var reward = Score.ScoreForEqualLeftRightDistance; // this is a parameter, change this when performing quality testing
        //     var isTerminalState = IsGameOver;
        //     var rotation = Input.Rotation;
        //     var distances = Raycasts.Distances;
        //
        //     var initialString = $"{reward.Round()};{isTerminalState.ToString().FirstLetterToUpper()};"
        //                         + $"{rotation.Round()}";
        //
        //     var stringBuilder = new StringBuilder(initialString);
        //     foreach (var raycast in distances)
        //     {
        //         stringBuilder.Append(";" + raycast.Round());
        //     }
        //     return stringBuilder.ToString();
        // }
        //
        // public string GetHeaders()
        // {
        //     return "Reward;IsTerminalState;Action(rotation);State(distances[9]);"; 
        // }
    }

    public class RaycastData
    {
        public float[] Distances;
    }

    public class ScoreData
    {
        public float ScoreForEqualLeftRightDistance;
        public float ScoreForBeingCloseToCenterOfTheRoad;
        public float TotalTime; // useful for comparing algorithms
        public float TotalDistance; // useful for comparing algorithms
    }
}