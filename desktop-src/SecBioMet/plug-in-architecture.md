---
title: Plug-in architecture
description: Biometric units expose the capabilities of a device to the framework through a standard interface that consists of sensor, engine, and storage adapters.
ms.assetid: d2835413-70a3-45fa-93e2-3fe78097554f
ms.topic: article
ms.date: 05/31/2018
---

# Plug-in architecture

Biometric devices are manufactured in a wide variety of types and configurations. The Windows Biometric Framework addresses this variety by providing an extensible architecture that enables third party developers to create custom plug-in components. The primary component is a software object called a biometric unit. Biometric units expose the capabilities of a device to the framework through a standard interface that consists of sensor, engine, and storage adapters. Biometric units and their constituent components are discussed in the following topics.

## Biometric unit

The central component of the Windows Biometric Framework plug-in architecture is the biometric unit, a software object that exposes the capabilities of a biometric device to the framework through a standard interface.

A single physical sensor is associated with each biometric unit. The sensor captures biometric data and may also, depending on its hardware capabilities, perform other biometric operations such as template matching and storage. Sensors that do not support onboard matching or storage require additional software modules to perform these functions. For more information, see [Adapters](/previous-versions//dd401508(v=vs.85)).

The following illustration shows how data flows through a biometric unit. Essentially, the data flow forms a type of pipeline. The initial input to the pipeline is a biometric sample captured by a physical sensor. The engine attempts to match the sample to templates that already exist in the template store or, if no match is found, builds a new template from repeated physical samples and saves the template in the store.

![data flowing through a biometric unit](images/biometricunit-dataflow.png)

## Biometric unit life cycle

### Creation

When the Windows Biometric Service starts or when it receives a hardware notification from the Plug and Play manager, it scans for any hardware that supports the well-known interface GUID\_DEVINTERFACE\_BIOMETRIC\_READER (E2B5183A-99EA-4cc3-AD6B-80CA8D715B80). For each biometric device discovered it then:

-   Opens a handle to the device.
-   Queries the device capabilities by using a Windows Biometric Driver control interface.
-   Opens the device registry key and attempts to locate information about any associated adapter plug-ins.
-   Opens the Windows Biometric Service registry key and searches for information about any global plug-ins that should override the device specific values found in the preceding step.
-   Builds a biometric unit to represent the device and passes the unit to a biometric service provider.

### Configuration

After a biometric service provider (BSP) accepts a biometric unit, it configures the unit and assigns it to a sensor pool. For more information, see [Sensor Pools](sensor-pools.md). The unit is configured by loading the appropriate adapters, connecting to a template store, and possibly changing the operating mode. A biometric unit can be configured to operate in one of two modes:

-   In the basic mode, the unit acts as a simple capture device. It does not use onboard processing or storage but relies entirely on software adapters for additional support. It should be able to generate samples in a standard format. For example, fingerprint readers should generate samples that comply with ANSI INCITS 381-2004. The purpose of the basic mode is to support interoperability among components from different vendors.
-   In the advanced mode, the biometric unit uses onboard processing and storage functions. It must expose the standard interfaces but can generate and process samples in any format desired.

When a biometric unit is moved from one sensor pool to another, its adapters are unloaded and it is reconfigured for the new sensor pool. The identity of the biometric unit remains constant; only the hardware configuration and adapter plug-ins change.

### Shut Down

When the Windows Biometric Service shuts down or when the Plug and Play manager notifies it that a unit has been removed, the service deletes all biometric units.

## Adapters

Plug-in software components called adapters connect a biometric unit to its underlying hardware and supply any functionality that may be missing from the sensor hardware. There are three types of adapters that you can create:

-   A sensor adapter wraps a biometric device and provides a standard interface for configuring the sensor, capturing samples, and controlling the flow of biometric data to the processing engine.
-   An engine adapter generates biometric templates from captured samples, matches samples to existing templates, and indexes templates.
-   A storage adapter manages template databases.

Adapters can be loaded and unloaded at runtime. This enables the Windows Biometric Service to dynamically reconfigure a biometric unit by connecting it to a different set of adapters.

Finally, each of the sensor, engine, and storage adapter interfaces expose two methods, **ControlUnit** and **ControlUnitPrivileged**, that enable client applications to access custom adapter capabilities defined by the vendor. This allows the vendor to define an almost unlimited set of control operations for a device. Further, by choosing which function to implement, a vendor can choose to make some control operations available to non-privileged users while restricting other operations to privileged users.

For more information about how to create adapters, see [Create adapter plug-ins](creating-adapter-plug-ins.md).

## Adapter performance requirements

Because the objective is fast response overall, the performance of an adapter isn't specified in terms of time limits on specific routines. Instead, performance is specified as a set of requirements for the overall user experience.

There are two requirements:

-   Any interaction between the user and the operating system that involves biometrics must complete within two seconds. That interval measures the start-to-finish time that the user perceives from the time they touch or swipe the sensor until the time something visible happens on the device screen. (For example, during unlock, there must be no more than a two-second delay between the user touching or swiping the fingerprint sensor and the lock screen acknowledging the user's identity.)
-   For the initial appearance of credential tiles on the sign-in or lock screen, we allow a little more time (three seconds, maximum), but we still prefer sooner rather than later. Specifically, the bio tile needs to be visible on screen within three seconds of the appearance of the lock or sign-in panel.

These numbers are not arbitrary. Numerous studies have shown that human beings tend to experience everything that happens within a two-second interval as part of the "now" moment. If event A and event B happen within two seconds of each other, people perceive those events as being simultaneous. If the events are separated by more than about three seconds, people think there's a delay—they feel that something is "taking too long." So this is an issue of hardwired human psychology.

 

 