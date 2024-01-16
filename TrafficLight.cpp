#include "TrafficLight.h"

ATrafficLight::ATrafficLight()
{
    PrimaryActorTick.bCanEverTick = true;

    // Initialize durations for each light state
    RedLightDuration = 10.0f;
    GreenLightDuration = 10.0f;
    YellowLightDuration = 3.0f;

    // Start with the red light
    CurrentState = LightState::Red;
}

void ATrafficLight::BeginPlay()
{
    Super::BeginPlay();
}

void ATrafficLight::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Update light state based on timers
    UpdateLight();
}

void ATrafficLight::ChangeLightState()
{
    // Switch to the next light state
    switch (CurrentState)
    {
    case LightState::Red:
        CurrentState = LightState::Green;
        break;
    case LightState::Green:
        CurrentState = LightState::Yellow;
        break;
    case LightState::Yellow:
        CurrentState = LightState::Red;
        break;
    }
}

void ATrafficLight::UpdateLight()
{
    static float Timer = 0;

    // Increment timer
    Timer += GetWorld()->DeltaTimeSeconds;

    // Change light state based on the timer
    switch (CurrentState)
    {
    case LightState::Red:
        if (Timer > RedLightDuration)
        {
            ChangeLightState();
            Timer = 0;
        }
        break;
    case LightState::Green:
        if (Timer > GreenLightDuration)
        {
            ChangeLightState();
            Timer = 0;
        }
        break;
    case LightState::Yellow:
        if (Timer > YellowLightDuration)
        {
            ChangeLightState();
            Timer = 0;
        }
        break;
    }

    // Logic to visually update the traffic light (e.g., change light color) goes here
}
