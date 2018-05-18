---
Description: 'Shows the members of the CXAPOParametersBase class.'
ms.assetid: 'C2113358-07DE-426E-AF26-BD8ED9902192'
title: CXAPOParametersBase Members
---

# CXAPOParametersBase Members

Shows the members of the [**CXAPOParametersBase**](cxapoparametersbase.md) class.

## Public Constructors



|                                                    |                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------|
| [**CXAPOParametersBase**](cxapoparametersbase.md) | Constructs a [**CXAPOParametersBase**](cxapoparametersbase.md) object. |



 

## Public Methods



|                                                                                                                              |                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddRef**](xaudio2.ixapo_interface_addref) (inherited from [**IXAPO**](ixapo.md))                                         | Increments the XAPO object's reference count.<br/>                                                                                                         |
| [**BeginProcess**](cxapoparametersbase-beginprocess.md)                                                                     | Returns the current process parameters. <br/>                                                                                                              |
| [**CalcInputFrames**](ixapo-interface-calcinputframes.md) (inherited from [**IXAPO**](ixapo.md))                           | Returns the number of input frames required to generate the given number of output frames.<br/>                                                            |
| [**CalcOutputFrames**](ixapo-interface-calcoutputframes.md) (inherited from [**IXAPO**](ixapo.md))                         | Returns the number of output frames required to generate the given number of input frames.<br/>                                                            |
| [**EndProcess**](cxapoparametersbase-endprocess.md)                                                                         | Notifies [**CXAPOParametersBase**](cxapoparametersbase.md) that the XAPO has finished accessing the current process parameters. <br/>                     |
| [**GetParameters**](ixapoparameters-interface-getparameters.md) (inherited from [**IXAPOParameters**](ixapoparameters.md)) | Gets effect-specific parameters. <br/>                                                                                                                     |
| [**GetRegistrationProperties**](ixapo-interface-getregistrationproperties.md) (inherited from [**IXAPO**](ixapo.md))       | Returns the registration properties of an XAPO.<br/>                                                                                                       |
| [**Initialize**](ixapo-interface-initialize.md) (inherited from [**IXAPO**](ixapo.md))                                     | Performs any effect-specific initialization.<br/>                                                                                                          |
| [**IsInputFormatSupported**](ixapo-interface-isinputformatsupported.md) (inherited from [**IXAPO**](ixapo.md))             | Queries if a specific input format is supported for a given output format.<br/>                                                                            |
| [**IsOutputFormatSupported**](ixapo-interface-isoutputformatsupported.md) (inherited from [**IXAPO**](ixapo.md))           | Queries if a specific output format is supported for a given input format.<br/>                                                                            |
| [**LockForProcess**](ixapo-interface-lockforprocess.md) (inherited from [**IXAPO**](ixapo.md))                             | Notifies XAPO of stream formats [**Process**](ixapo-interface-process.md) will be given.<br/>                                                             |
| [**OnSetParameters**](cxapoparametersbase-onsetparameters.md)                                                               | Called by [**IXAPOParameters::SetParameters**](ixapoparameters-interface-setparameters.md) to allow for user-defined parameter validation. <br/>          |
| [**ParametersChanged**](cxapoparametersbase-parameterschanged.md)                                                           | Indicates if [**IXAPOParameters::SetParameters**](ixapoparameters-interface-setparameters.md) has been called since the last processing pass. <br/>       |
| [**QueryInterface**](xaudio2.ixapo_interface_queryinterface) (inherited from [**IXAPO**](ixapo.md))                         | Retrieves the requested interface pointer if the XAPO supports it.<br/>                                                                                    |
| [**Release**](xaudio2.ixapo_interface_release) (inherited from [**IXAPO**](ixapo.md))                                       | Decrements the XAPO object's reference count and deletes the object if the reference count falls to zero.<br/>                                             |
| [**Reset**](ixapo-interface-reset.md) (inherited from [**IXAPO**](ixapo.md))                                               | Returns the object to the state it was in just after [**LockForProcess**](ixapo-interface-lockforprocess.md) was called.<br/>                             |
| [**SetParameters**](ixapoparameters-interface-setparameters.md) (inherited from [**IXAPOParameters**](ixapoparameters.md)) | Sets effect-specific parameters.<br/>                                                                                                                      |
| [**UnlockForProcess**](ixapo-interface-unlockforprocess.md) (inherited from [**IXAPO**](ixapo.md))                         | Opposite of LockForProcess: variables allocated during [**LockForProcess**](ixapo-interface-lockforprocess.md) should be deallocated in this method.<br/> |



 

## Related topics

<dl> <dt>

[**CXAPOParametersBase class**](cxapoparametersbase.md)
</dt> </dl>

 

 




