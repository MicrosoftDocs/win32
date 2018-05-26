---
title: Runtime Power Management Routines
description: Runtime Power Management Routines
ms.assetid: 42C2E806-7BF4-4874-83D6-705FFBBD0992
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Runtime Power Management Routines

## 

This section lists the runtime power management routines supplied by the Storport driver.

## In this section



| Topic                                                                                     | Description                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**StorPortInitializePoFxPower**](storportinitializepofxpower.md)<br/>             | A miniport driver calls **StorPortInitializePoFxPower** to register a storage device with the power management framework (PoFx).<br/>                                                                                 |
| [**StorPortPoFxActivateComponent**](storportpofxactivatecomponent.md)<br/>         | The **StorPortPoFxActivateComponent** routine increments the activation reference count on the specified component of a storage device.<br/>                                                                          |
| [**StorPortPoFxIdleComponent**](storportpofxidlecomponent.md)<br/>                 | The **StorPortPoFxIdleComponent** routine decrements the activation reference count of a specified component of a storage device.<br/>                                                                                |
| [**StorPortPoFxPowerControl**](storportpofxpowercontrol.md)<br/>                   | The **StorPortPoFxPowerControl** routine sends a power control request to the power management framework (PoFx) to forward to the power engine plug-in (PEP).<br/>                                                    |
| [**StorPortPoFxSetComponentLatency**](storportpofxsetcomponentlatency.md)<br/>     | The **StorPortPoFxSetComponentLatency** routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified storage device component.<br/> |
| [**StorPortPoFxSetComponentResidency**](storportpofxsetcomponentresidency.md)<br/> | The **StorPortPoFxSetComponentResidency** routine sets the estimated time for how long a storage device component is likely to remain idle after the component enters the idle condition.<br/>                        |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Runtime%20Power%20Management%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





