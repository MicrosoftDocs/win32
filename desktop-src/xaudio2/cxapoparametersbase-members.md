---
Description: Shows the members of the CXAPOParametersBase class.
ms.assetid: C2113358-07DE-426E-AF26-BD8ED9902192
title: CXAPOParametersBase Members
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CXAPOParametersBase Members

Shows the members of the [**CXAPOParametersBase**](/windows/win32/XAPOBase/nl-xapobase-cxapoparametersbase?branch=master) class.

## Public Constructors



|                                                    |                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------|
| [**CXAPOParametersBase**](/windows/win32/XAPOBase/nl-xapobase-cxapoparametersbase?branch=master) | Constructs a [**CXAPOParametersBase**](/windows/win32/XAPOBase/nl-xapobase-cxapoparametersbase?branch=master) object. |



 

## Public Methods



|                                                                                                                              |                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddRef**](xaudio2.ixapo_interface_addref) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                                         | Increments the XAPO object's reference count.<br/>                                                                                                         |
| [**BeginProcess**](cxapoparametersbase-beginprocess.md)                                                                     | Returns the current process parameters. <br/>                                                                                                              |
| [**CalcInputFrames**](ixapo-interface-calcinputframes.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                           | Returns the number of input frames required to generate the given number of output frames.<br/>                                                            |
| [**CalcOutputFrames**](ixapo-interface-calcoutputframes.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                         | Returns the number of output frames required to generate the given number of input frames.<br/>                                                            |
| [**EndProcess**](cxapoparametersbase-endprocess.md)                                                                         | Notifies [**CXAPOParametersBase**](/windows/win32/XAPOBase/nl-xapobase-cxapoparametersbase?branch=master) that the XAPO has finished accessing the current process parameters. <br/>                     |
| [**GetParameters**](ixapoparameters-interface-getparameters.md) (inherited from [**IXAPOParameters**](/windows/win32/XAPO/nn-xapo-ixapoparameters?branch=master)) | Gets effect-specific parameters. <br/>                                                                                                                     |
| [**GetRegistrationProperties**](ixapo-interface-getregistrationproperties.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))       | Returns the registration properties of an XAPO.<br/>                                                                                                       |
| [**Initialize**](ixapo-interface-initialize.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                                     | Performs any effect-specific initialization.<br/>                                                                                                          |
| [**IsInputFormatSupported**](ixapo-interface-isinputformatsupported.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))             | Queries if a specific input format is supported for a given output format.<br/>                                                                            |
| [**IsOutputFormatSupported**](ixapo-interface-isoutputformatsupported.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))           | Queries if a specific output format is supported for a given input format.<br/>                                                                            |
| [**LockForProcess**](ixapo-interface-lockforprocess.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                             | Notifies XAPO of stream formats [**Process**](ixapo-interface-process.md) will be given.<br/>                                                             |
| [**OnSetParameters**](cxapoparametersbase-onsetparameters.md)                                                               | Called by [**IXAPOParameters::SetParameters**](ixapoparameters-interface-setparameters.md) to allow for user-defined parameter validation. <br/>          |
| [**ParametersChanged**](cxapoparametersbase-parameterschanged.md)                                                           | Indicates if [**IXAPOParameters::SetParameters**](ixapoparameters-interface-setparameters.md) has been called since the last processing pass. <br/>       |
| [**QueryInterface**](xaudio2.ixapo_interface_queryinterface) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                         | Retrieves the requested interface pointer if the XAPO supports it.<br/>                                                                                    |
| [**Release**](xaudio2.ixapo_interface_release) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                                       | Decrements the XAPO object's reference count and deletes the object if the reference count falls to zero.<br/>                                             |
| [**Reset**](ixapo-interface-reset.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                                               | Returns the object to the state it was in just after [**LockForProcess**](ixapo-interface-lockforprocess.md) was called.<br/>                             |
| [**SetParameters**](ixapoparameters-interface-setparameters.md) (inherited from [**IXAPOParameters**](/windows/win32/XAPO/nn-xapo-ixapoparameters?branch=master)) | Sets effect-specific parameters.<br/>                                                                                                                      |
| [**UnlockForProcess**](ixapo-interface-unlockforprocess.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                         | Opposite of LockForProcess: variables allocated during [**LockForProcess**](ixapo-interface-lockforprocess.md) should be deallocated in this method.<br/> |



 

## Related topics

<dl> <dt>

[**CXAPOParametersBase class**](/windows/win32/XAPOBase/nl-xapobase-cxapoparametersbase?branch=master)
</dt> </dl>

 

 




