---
description: Shows the members of the CXAPOBase class.
ms.assetid: 0791888B-7215-475B-95C8-B558A1E57783
title: CXAPOBase Members
ms.topic: article
ms.date: 05/31/2018
---

# CXAPOBase Members

Shows the members of the [**CXAPOBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapobase) class.

## Public Constructors



|   Constructor                             |              Description                                       |
|--------------------------------|-----------------------------------------------------|
| [**CXAPOBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapobase) | Constructs a [**CXAPOBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapobase) object. |



 

## Public Methods



|     Method                                                                                                                   |     Description                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddRef**](/previous-versions/windows/desktop/legacy/ee418448(v=vs.85)) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                   | Increments the XAPO object's reference count.<br/>                                                                                                         |
| [**CalcInputFrames**](/windows/win32/api/xapo/nf-xapo-ixapo-calcinputframes) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                     | Returns the number of input frames required to generate the given number of output frames.<br/>                                                            |
| [**CalcOutputFrames**](/windows/win32/api/xapo/nf-xapo-ixapo-calcoutputframes) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                   | Returns the number of output frames required to generate the given number of input frames.<br/>                                                            |
| [**GetRegistrationProperties**](/windows/win32/api/xapo/nf-xapo-ixapo-getregistrationproperties) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo)) | Returns the registration properties of an XAPO.<br/>                                                                                                       |
| [**Initialize**](/windows/win32/api/xapo/nf-xapo-ixapo-initialize) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                               | Performs any effect-specific initialization.<br/>                                                                                                          |
| [**IsInputFormatSupported**](/windows/win32/api/xapo/nf-xapo-ixapo-isinputformatsupported) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))       | Queries if a specific input format is supported for a given output format.<br/>                                                                            |
| [**IsOutputFormatSupported**](/windows/win32/api/xapo/nf-xapo-ixapo-isoutputformatsupported) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))     | Queries if a specific output format is supported for a given input format.<br/>                                                                            |
| [**LockForProcess**](/windows/win32/api/xapo/nf-xapo-ixapo-lockforprocess) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                       | Notifies XAPO of stream formats [**Process**](/windows/win32/api/xapo/nf-xapo-ixapo-process) will be given.<br/>                                                             |
| [**QueryInterface**](/previous-versions/windows/desktop/legacy/ee418457(v=vs.85)) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                   | Retrieves the requested interface pointer if the XAPO supports it.<br/>                                                                                    |
| [**Release**](/previous-versions/windows/desktop/legacy/ee418458(v=vs.85)) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                 | Decrements the XAPO object's reference count and deletes the object if the reference count falls to zero.<br/>                                             |
| [**Reset**](/windows/win32/api/xapo/nf-xapo-ixapo-reset) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                         | Returns the object to the state it was in just after [**LockForProcess**](/windows/win32/api/xapo/nf-xapo-ixapo-lockforprocess) was called.<br/>                             |
| [**UnlockForProcess**](/windows/win32/api/xapo/nf-xapo-ixapo-unlockforprocess) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                   | Opposite of LockForProcess: variables allocated during [**LockForProcess**](/windows/win32/api/xapo/nf-xapo-ixapo-lockforprocess) should be deallocated in this method.<br/> |



 

## Protected Methods



|      Method                                                                                    |     Description                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetRegistrationPropertiesInternal**](/windows/win32/api/xapobase/nf-xapobase-cxapobase-getregistrationpropertiesinternal) | Returns a pointer to the [**XAPO\_REGISTRATION\_PROPERTIES**](/windows/desktop/api/xapo/ns-xapo-xapo_registration_properties)S structure containing the registration properties the XAPO was created with.<br/> |
| [**IsLocked**](/windows/win32/api/xapobase/nf-xapobase-cxapobase-islocked)                                                   | Checks if the XAPO is locked.<br/>                                                                                                                                                |
| LONG m\_lReferenceCount<br/>                                                       | The XAPO object's COM reference count.<br/>                                                                                                                                       |
| [**ProcessThru**](/windows/win32/api/xapobase/nf-xapobase-cxapobase-processthru)                                             | Called by an [**IXAPO::Process**](/windows/win32/api/xapo/nf-xapo-ixapo-process) implementation when an XAPO is disabled for thru processing.<br/>                                                  |
| [**ValidateFormatDefault**](/windows/win32/api/xapobase/nf-xapobase-cxapobase-validateformatdefault)                         | Verifies that an audio format falls within the default ranges supported.<br/>                                                                                                     |
| [**ValidateFormatPair**](/windows/win32/api/xapobase/nf-xapobase-cxapobase-validateformatpair)                               | Verifies that an input and output format pair configuration is supported with respect to the XAPO property flags.<br/>                                                            |



 

## Related topics

<dl> <dt>

[**CXAPOBase class**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapobase)
</dt> </dl>

 

 
