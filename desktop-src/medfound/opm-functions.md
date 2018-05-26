---
Description: The following functions are used with Output Protection Manager (OPM).
ms.assetid: 7ecde6ae-56fd-451b-bebb-224c6801be05
title: OPM Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OPM Functions

The following functions are used with [Output Protection Manager](output-protection-manager.md) (OPM).



| Function                                                                                             | Description                                                                                                                           |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**OPMGetVideoOutputForTarget**](/windows/win32/opmapi/nf-opmapi-opmgetvideooutputfortarget?branch=master)                                     | Returns a video output object for the VidPN target on the specified adapter.                                                          |
| [**OPMGetVideoOutputsFromHMONITOR**](/windows/win32/opmapi/nf-opmapi-opmgetvideooutputsfromhmonitor?branch=master)                             | Creates an Output Protection Manager (OPM) object for each physical monitor that is associated with a particular **HMONITOR** handle. |
| [**OPMGetVideoOutputsFromIDirect3DDevice9Object**](/windows/win32/opmapi/nf-opmapi-opmgetvideooutputsfromidirect3ddevice9object?branch=master) | Creates an OPM object for each physical monitor that is associated with a particular Direct3D device.                                 |



 

The following functions are used by OPM to access functionality in the display driver. Applications should not call these functions.

-   [**ConfigureOPMProtectedOutput**](configureopmprotectedoutput.md)
-   [**CreateOPMProtectedOutputs**](createopmprotectedoutputs.md)
-   [**DestroyOPMProtectedOutput**](destroyopmprotectedoutput.md)
-   [**GetCertificate**](/windows/win32/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-getcertificate?branch=master)
-   [**GetCertificateSize**](/windows/win32/d3d9/nf-d3d9-idirect3dauthenticatedchannel9-getcertificatesize?branch=master)
-   [**GetCOPPCompatibleOPMInformation**](getcoppcompatibleopminformation.md)
-   [**GetOPMInformation**](getopminformation.md)
-   [**GetOPMRandomNumber**](getopmrandomnumber.md)
-   [**GetSuggestedOPMProtectedOutputArraySize**](getsuggestedopmprotectedoutputarraysize.md)
-   [**SetOPMSigningKeyAndSequenceNumbers**](setopmsigningkeyandsequencenumbers.md)

## Related topics

<dl> <dt>

[OPM Programming Reference](opm-programming-reference.md)
</dt> <dt>

[Output Protection Manager](output-protection-manager.md)
</dt> </dl>

 

 



