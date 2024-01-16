#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "TrafficLight.generated.h"

UCLASS()
class YOURPROJECTNAME_API ATrafficLight : public AActor
{
    GENERATED_BODY()
    
public:    
    ATrafficLight();

protected:
    virtual void BeginPlay() override;

public:    
    virtual void Tick(float DeltaTime) override;

    // Function to change the traffic light state
    void ChangeLightState();

private:
    // Traffic light states
    enum class LightState { Red, Yellow, Green };
    LightState CurrentState;

    // Timers for light changes
    float RedLightDuration;
    float GreenLightDuration;
    float YellowLightDuration;

    // Function to update the light based on the current state
    void UpdateLight();
};
