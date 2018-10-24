---
Description: This section contains an alphabetic list of the available line device functions in the Telephony SPI.
ms.assetid: 2a27fbb7-93b5-4106-afd3-e63456650fb9
title: TSPI Line Device Functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TSPI Line Device Functions

This section contains an alphabetic list of the available line device functions in the Telephony SPI. The information for each function includes the following:

-   A statement of the function's purpose.
-   The correct syntax for the function.
-   A description of the function's parameters, including valid call states.
-   A description of the function's return value.
-   A Remarks section that can include any or all of the following: a list of the valid call states on entry of the function and typical call state transitions when the request completes; a description of which members of large data structures must be filled in by the service provider and which members must have their values preserved intact; and comparison with a corresponding function within TAPI.
-   References to other functions, messages, or data structures.
    > [!Note]  
    > The actual states in which a function can be performed may be limited by the capabilities of the service provider. Service providers must set the **dwCallFeatures** member in the [**LINECALLSTATUS**](https://msdn.microsoft.com/en-us/library/ms735544(v=VS.85).aspx) structure, the **dwAddressFeatures** member in the [**LINEADDRESSSTATUS**](https://msdn.microsoft.com/en-us/library/ms734938(v=VS.85).aspx) structure, and the **dwLineFeatures** member in the [**LINEDEVSTATUS**](https://msdn.microsoft.com/en-us/library/ms735610(v=VS.85).aspx) structure to indicate to applications whether or not a function is permitted at that point in time.

     

This section contains the following TSPI line device functions:

-   [**TSPI\_lineAccept**](https://msdn.microsoft.com/en-us/library/ms725527(v=VS.85).aspx)
-   [**TSPI\_lineAddToConference**](https://msdn.microsoft.com/en-us/library/ms725528(v=VS.85).aspx)
-   [**TSPI\_lineAnswer**](https://msdn.microsoft.com/en-us/library/ms725529(v=VS.85).aspx)
-   [**TSPI\_lineBlindTransfer**](https://msdn.microsoft.com/en-us/library/ms725530(v=VS.85).aspx)
-   [**TSPI\_lineClose**](https://msdn.microsoft.com/en-us/library/ms725531(v=VS.85).aspx)
-   [**TSPI\_lineCloseCall**](https://msdn.microsoft.com/en-us/library/ms725532(v=VS.85).aspx)
-   [**TSPI\_lineCloseMSPInstance**](https://msdn.microsoft.com/en-us/library/ms725533(v=VS.85).aspx)
-   [**TSPI\_lineCompleteCall**](https://msdn.microsoft.com/en-us/library/ms725534(v=VS.85).aspx)
-   [**TSPI\_lineCompleteTransfer**](https://msdn.microsoft.com/en-us/library/ms725535(v=VS.85).aspx)
-   [**TSPI\_lineConditionalMediaDetection**](https://msdn.microsoft.com/en-us/library/ms725536(v=VS.85).aspx)
-   [**TSPI\_lineConfigDialog**](https://msdn.microsoft.com/en-us/library/ms725537(v=VS.85).aspx)
-   [**TSPI\_lineConfigDialogEdit**](https://msdn.microsoft.com/en-us/library/ms725538(v=VS.85).aspx)
-   [**TSPI\_lineCreateMSPInstance**](https://msdn.microsoft.com/en-us/library/ms725539(v=VS.85).aspx)
-   [**TSPI\_lineDevSpecific**](https://msdn.microsoft.com/en-us/library/ms725540(v=VS.85).aspx)
-   [**TSPI\_lineDevSpecificFeature**](https://msdn.microsoft.com/en-us/library/ms725541(v=VS.85).aspx)
-   [**TSPI\_lineDial**](https://msdn.microsoft.com/en-us/library/ms725542(v=VS.85).aspx)
-   [**TSPI\_lineDrop**](https://msdn.microsoft.com/en-us/library/ms725543(v=VS.85).aspx)
-   [TSPI\_lineDropNoOwner](tspi-linedropnoowner.md)
-   [TSPI\_lineDropOnClose](tspi-linedroponclose.md)
-   [**TSPI\_lineForward**](https://msdn.microsoft.com/en-us/library/ms725546(v=VS.85).aspx)
-   [**TSPI\_lineGatherDigits**](https://msdn.microsoft.com/en-us/library/ms725547(v=VS.85).aspx)
-   [**TSPI\_lineGenerateDigits**](https://msdn.microsoft.com/en-us/library/ms725548(v=VS.85).aspx)
-   [**TSPI\_lineGenerateTone**](https://msdn.microsoft.com/en-us/library/ms725549(v=VS.85).aspx)
-   [**TSPI\_lineGetAddressCaps**](https://msdn.microsoft.com/en-us/library/ms725560(v=VS.85).aspx)
-   [**TSPI\_lineGetAddressID**](https://msdn.microsoft.com/en-us/library/ms725561(v=VS.85).aspx)
-   [**TSPI\_lineGetAddressStatus**](https://msdn.microsoft.com/en-us/library/ms725562(v=VS.85).aspx)
-   [**TSPI\_lineGetCallAddressID**](https://msdn.microsoft.com/en-us/library/ms725563(v=VS.85).aspx)
-   [**TSPI\_lineGetCallHubTracking**](https://msdn.microsoft.com/en-us/library/ms725564(v=VS.85).aspx)
-   [**TSPI\_lineGetCallIDs**](https://msdn.microsoft.com/en-us/library/ms725565(v=VS.85).aspx)
-   [**TSPI\_lineGetCallInfo**](https://msdn.microsoft.com/en-us/library/ms725566(v=VS.85).aspx)
-   [**TSPI\_lineGetCallStatus**](https://msdn.microsoft.com/en-us/library/ms725567(v=VS.85).aspx)
-   [**TSPI\_lineGetDevCaps**](https://msdn.microsoft.com/en-us/library/ms725568(v=VS.85).aspx)
-   [**TSPI\_lineGetDevConfig**](https://msdn.microsoft.com/en-us/library/ms725569(v=VS.85).aspx)
-   [**TSPI\_lineGetExtensionID**](https://msdn.microsoft.com/en-us/library/ms725570(v=VS.85).aspx)
-   [**TSPI\_lineGetIcon**](https://msdn.microsoft.com/en-us/library/ms725571(v=VS.85).aspx)
-   [**TSPI\_lineGetID**](https://msdn.microsoft.com/en-us/library/ms725572(v=VS.85).aspx)
-   [**TSPI\_lineGetLineDevStatus**](https://msdn.microsoft.com/en-us/library/ms725573(v=VS.85).aspx)
-   [**TSPI\_lineGetNumAddressIDs**](https://msdn.microsoft.com/en-us/library/ms725574(v=VS.85).aspx)
-   [**TSPI\_lineHold**](https://msdn.microsoft.com/en-us/library/ms725575(v=VS.85).aspx)
-   [**TSPI\_lineMakeCall**](https://msdn.microsoft.com/en-us/library/ms725576(v=VS.85).aspx)
-   [**TSPI\_lineMonitorDigits**](https://msdn.microsoft.com/en-us/library/ms725577(v=VS.85).aspx)
-   [**TSPI\_lineMonitorMedia**](https://msdn.microsoft.com/en-us/library/ms725578(v=VS.85).aspx)
-   [**TSPI\_lineMonitorTones**](https://msdn.microsoft.com/en-us/library/ms725579(v=VS.85).aspx)
-   [**TSPI\_lineMSPIdentify**](https://msdn.microsoft.com/en-us/library/ms725580(v=VS.85).aspx)
-   [**TSPI\_lineNegotiateExtVersion**](https://msdn.microsoft.com/en-us/library/ms725581(v=VS.85).aspx)
-   [**TSPI\_lineNegotiateTSPIVersion**](https://msdn.microsoft.com/en-us/library/ms725582(v=VS.85).aspx)
-   [**TSPI\_lineOpen**](https://msdn.microsoft.com/en-us/library/ms725583(v=VS.85).aspx)
-   [**TSPI\_linePark**](https://msdn.microsoft.com/en-us/library/ms725584(v=VS.85).aspx)
-   [**TSPI\_linePickup**](https://msdn.microsoft.com/en-us/library/ms725585(v=VS.85).aspx)
-   [**TSPI\_linePrepareAddToConference**](https://msdn.microsoft.com/en-us/library/ms725586(v=VS.85).aspx)
-   [**TSPI\_lineReceiveMSPData**](https://msdn.microsoft.com/en-us/library/ms725587(v=VS.85).aspx)
-   [**TSPI\_lineRedirect**](https://msdn.microsoft.com/en-us/library/ms725588(v=VS.85).aspx)
-   [**TSPI\_lineReleaseUserUserInfo**](https://msdn.microsoft.com/en-us/library/ms725589(v=VS.85).aspx)
-   [**TSPI\_lineRemoveFromConference**](https://msdn.microsoft.com/en-us/library/ms725590(v=VS.85).aspx)
-   [**TSPI\_lineSecureCall**](https://msdn.microsoft.com/en-us/library/ms725591(v=VS.85).aspx)
-   [**TSPI\_lineSelectExtVersion**](https://msdn.microsoft.com/en-us/library/ms725592(v=VS.85).aspx)
-   [**TSPI\_lineSendUserUserInfo**](https://msdn.microsoft.com/en-us/library/ms725593(v=VS.85).aspx)
-   [**TSPI\_lineSetAppSpecific**](https://msdn.microsoft.com/en-us/library/ms725594(v=VS.85).aspx)
-   [**TSPI\_lineSetCallData**](https://msdn.microsoft.com/en-us/library/ms725595(v=VS.85).aspx)
-   [**TSPI\_lineSetCallHubTracking**](https://msdn.microsoft.com/en-us/library/ms725596(v=VS.85).aspx)
-   [**TSPI\_lineSetCallParams**](https://msdn.microsoft.com/en-us/library/ms725597(v=VS.85).aspx)
-   [**TSPI\_lineSetCallQualityOfService**](https://msdn.microsoft.com/en-us/library/ms725598(v=VS.85).aspx)
-   [**TSPI\_lineSetCallTreatment**](https://msdn.microsoft.com/en-us/library/ms725599(v=VS.85).aspx)
-   [TSPI\_lineSetCurrentLocation](tspi-linesetcurrentlocation.md)
-   [**TSPI\_lineSetDefaultMediaDetection**](https://msdn.microsoft.com/en-us/library/ms725601(v=VS.85).aspx)
-   [**TSPI\_lineSetDevConfig**](https://msdn.microsoft.com/en-us/library/ms725602(v=VS.85).aspx)
-   [**TSPI\_lineSetLineDevStatus**](https://msdn.microsoft.com/en-us/library/ms725603(v=VS.85).aspx)
-   [**TSPI\_lineSetMediaControl**](https://msdn.microsoft.com/en-us/library/ms725604(v=VS.85).aspx)
-   [**TSPI\_lineSetMediaMode**](https://msdn.microsoft.com/en-us/library/ms725605(v=VS.85).aspx)
-   [**TSPI\_lineSetStatusMessages**](https://msdn.microsoft.com/en-us/library/ms725606(v=VS.85).aspx)
-   [**TSPI\_lineSetTerminal**](https://msdn.microsoft.com/en-us/library/ms725607(v=VS.85).aspx)
-   [**TSPI\_lineSetupConference**](https://msdn.microsoft.com/en-us/library/ms725608(v=VS.85).aspx)
-   [**TSPI\_lineSetupTransfer**](https://msdn.microsoft.com/en-us/library/ms725609(v=VS.85).aspx)
-   [**TSPI\_lineSwapHold**](https://msdn.microsoft.com/en-us/library/ms725610(v=VS.85).aspx)
-   [**TSPI\_lineUncompleteCall**](https://msdn.microsoft.com/en-us/library/ms725611(v=VS.85).aspx)
-   [**TSPI\_lineUnhold**](https://msdn.microsoft.com/en-us/library/ms725612(v=VS.85).aspx)
-   [**TSPI\_lineUnpark**](https://msdn.microsoft.com/en-us/library/ms725613(v=VS.85).aspx)

 

 



