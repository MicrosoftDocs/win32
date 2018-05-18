---
Description: 'The following functions are used with Output Protection Manager (OPM).'
ms.assetid: '7ecde6ae-56fd-451b-bebb-224c6801be05'
title: OPM Functions
---

# OPM Functions

The following functions are used with [Output Protection Manager](output-protection-manager.md) (OPM).



| Function                                                                                             | Description                                                                                                                           |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**OPMGetVideoOutputForTarget**](opmgetvideooutputfortarget.md)                                     | Returns a video output object for the VidPN target on the specified adapter.                                                          |
| [**OPMGetVideoOutputsFromHMONITOR**](opmgetvideooutputsfromhmonitor.md)                             | Creates an Output Protection Manager (OPM) object for each physical monitor that is associated with a particular **HMONITOR** handle. |
| [**OPMGetVideoOutputsFromIDirect3DDevice9Object**](opmgetvideooutputsfromidirect3ddevice9object.md) | Creates an OPM object for each physical monitor that is associated with a particular Direct3D device.                                 |



 

The following functions are used by OPM to access functionality in the display driver. Applications should not call these functions.

-   [**ConfigureOPMProtectedOutput**](configureopmprotectedoutput.md)
-   [**CreateOPMProtectedOutputs**](createopmprotectedoutputs.md)
-   [**DestroyOPMProtectedOutput**](destroyopmprotectedoutput.md)
-   [**GetCertificate**](idirect3dauthenticatedchannel9-getcertificate.md)
-   [**GetCertificateSize**](idirect3dauthenticatedchannel9-getcertificatesize.md)
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

 

 



