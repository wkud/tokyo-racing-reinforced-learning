using System;
using ReinforcedLearning;

namespace TestUnityEnvironment
{
    class Program
    {
        static void Main(string[] args)
        {
            var ai = new AiSystem(0.25f, 0.85f, 0.7f);
            var env = new Environment(ai);
            
            for (int i = 0; i < 1000; i++)
            {
                env.TakeSimulationStep();
                var rot = env.MovementVector.Rotation;
                Console.WriteLine(rot);
            }
            
            Console.WriteLine("Finished");
        }
    }
}