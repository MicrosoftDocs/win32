---
Description: Shows the members of the CXAPOBase class.
ms.assetid: 0791888B-7215-475B-95C8-B558A1E57783
title: CXAPOBase Members
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CXAPOBase Members

Shows the members of the [**CXAPOBase**](/windows/win32/XAPOBase/nl-xapobase-cxapobase?branch=master) class.

## Public Constructors



|                                |                                                     |
|--------------------------------|-----------------------------------------------------|
| [**CXAPOBase**](/windows/win32/XAPOBase/nl-xapobase-cxapobase?branch=master) | Constructs a [**CXAPOBase**](/windows/win32/XAPOBase/nl-xapobase-cxapobase?branch=master) object. |



 

## Public Methods



|                                                                                                                        |                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddRef**](xaudio2.ixapo_interface_addref) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                                   | Increments the XAPO object's reference count.<br/>                                                                                                         |
| [**CalcInputFrames**](ixapo-interface-calcinputframes.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                     | Returns the number of input frames required to generate the given number of output frames.<br/>                                                            |
| [**CalcOutputFrames**](ixapo-interface-calcoutputframes.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                   | Returns the number of output frames required to generate the given number of input frames.<br/>                                                            |
| [**GetRegistrationProperties**](ixapo-interface-getregistrationproperties.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master)) | Returns the registration properties of an XAPO.<br/>                                                                                                       |
| [**Initialize**](ixapo-interface-initialize.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                               | Performs any effect-specific initialization.<br/>                                                                                                          |
| [**IsInputFormatSupported**](ixapo-interface-isinputformatsupported.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))       | Queries if a specific input format is supported for a given output format.<br/>                                                                            |
| [**IsOutputFormatSupported**](ixapo-interface-isoutputformatsupported.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))     | Queries if a specific output format is supported for a given input format.<br/>                                                                            |
| [**LockForProcess**](ixapo-interface-lockforprocess.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                       | Notifies XAPO of stream formats [**Process**](ixapo-interface-process.md) will be given.<br/>                                                             |
| [**QueryInterface**](xaudio2.ixapo_interface_queryinterface) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                   | Retrieves the requested interface pointer if the XAPO supports it.<br/>                                                                                    |
| [**Release**](xaudio2.ixapo_interface_release) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                                 | Decrements the XAPO object's reference count and deletes the object if the reference count falls to zero.<br/>                                             |
| [**Reset**](ixapo-interface-reset.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                                         | Returns the object to the state it was in just after [**LockForProcess**](ixapo-interface-lockforprocess.md) was called.<br/>                             |
| [**UnlockForProcess**](ixapo-interface-unlockforprocess.md) (inherited from [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master))                   | Opposite of LockForProcess: variables allocated during [**LockForProcess**](ixapo-interface-lockforprocess.md) should be deallocated in this method.<br/> |



 

## Protected Methods



|                                                                                          |                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetRegistrationPropertiesInternal**](cxapobase-getregistrationpropertiesinternal.md) | Returns a pointer to the [**XAPO\_REGISTRATION\_PROPERTIES**](/windows/win32/xapo/ns-xapo-xapo_registration_properties?branch=master)S structure containing the registration properties the XAPO was created with.<br/> |
| [**IsLocked**](cxapobase-islocked.md)                                                   | Checks if the XAPO is locked.<br/>                                                                                                                                                |
| LONG m\_lReferenceCount<br/>                                                       | The XAPO object's COM reference count.<br/>                                                                                                                                       |
| [**ProcessThru**](cxapobase-processthru.md)                                             | Called by an [**IXAPO::Process**](ixapo-interface-process.md) implementation when an XAPO is disabled for thru processing.<br/>                                                  |
| [**ValidateFormatDefault**](cxapobase-validateformatdefault.md)                         | Verifies that an audio format falls within the default ranges supported.<br/>                                                                                                     |
| [**ValidateFormatPair**](cxapobase-validateformatpair.md)                               | Verifies that an input and output format pair configuration is supported with respect to the XAPO property flags.<br/>                                                            |



 

## Related topics

<dl> <dt>

[**CXAPOBase class**](/windows/win32/XAPOBase/nl-xapobase-cxapobase?branch=master)
</dt> </dl>

 

 




