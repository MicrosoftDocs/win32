---
Description: Shows the members of the CXAPOBase class.
ms.assetid: 0791888B-7215-475B-95C8-B558A1E57783
title: CXAPOBase Members
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CXAPOBase Members

Shows the members of the [**CXAPOBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapobase) class.

## Public Constructors



|                                |                                                     |
|--------------------------------|-----------------------------------------------------|
| [**CXAPOBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapobase) | Constructs a [**CXAPOBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapobase) object. |



 

## Public Methods



|                                                                                                                        |                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddRef**](https://www.bing.com/search?q=**AddRef**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                   | Increments the XAPO object's reference count.<br/>                                                                                                         |
| [**CalcInputFrames**](https://msdn.microsoft.com/en-us/library/Ee418449(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                     | Returns the number of input frames required to generate the given number of output frames.<br/>                                                            |
| [**CalcOutputFrames**](https://msdn.microsoft.com/en-us/library/Ee418450(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                   | Returns the number of output frames required to generate the given number of input frames.<br/>                                                            |
| [**GetRegistrationProperties**](https://msdn.microsoft.com/en-us/library/Ee418451(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo)) | Returns the registration properties of an XAPO.<br/>                                                                                                       |
| [**Initialize**](https://msdn.microsoft.com/en-us/library/Ee418452(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                               | Performs any effect-specific initialization.<br/>                                                                                                          |
| [**IsInputFormatSupported**](https://msdn.microsoft.com/en-us/library/Ee418453(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))       | Queries if a specific input format is supported for a given output format.<br/>                                                                            |
| [**IsOutputFormatSupported**](https://msdn.microsoft.com/en-us/library/Ee418454(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))     | Queries if a specific output format is supported for a given input format.<br/>                                                                            |
| [**LockForProcess**](https://msdn.microsoft.com/en-us/library/Ee418455(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                       | Notifies XAPO of stream formats [**Process**](https://msdn.microsoft.com/en-us/library/Ee418456(v=VS.85).aspx) will be given.<br/>                                                             |
| [**QueryInterface**](https://www.bing.com/search?q=**QueryInterface**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                   | Retrieves the requested interface pointer if the XAPO supports it.<br/>                                                                                    |
| [**Release**](https://www.bing.com/search?q=**Release**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                 | Decrements the XAPO object's reference count and deletes the object if the reference count falls to zero.<br/>                                             |
| [**Reset**](https://msdn.microsoft.com/en-us/library/Ee418459(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                         | Returns the object to the state it was in just after [**LockForProcess**](https://msdn.microsoft.com/en-us/library/Ee418455(v=VS.85).aspx) was called.<br/>                             |
| [**UnlockForProcess**](https://msdn.microsoft.com/en-us/library/Ee418460(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                   | Opposite of LockForProcess: variables allocated during [**LockForProcess**](https://msdn.microsoft.com/en-us/library/Ee418455(v=VS.85).aspx) should be deallocated in this method.<br/> |



 

## Protected Methods



|                                                                                          |                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetRegistrationPropertiesInternal**](https://msdn.microsoft.com/en-us/library/Ee416375(v=VS.85).aspx) | Returns a pointer to the [**XAPO\_REGISTRATION\_PROPERTIES**](/windows/desktop/api/xapo/ns-xapo-xapo_registration_properties)S structure containing the registration properties the XAPO was created with.<br/> |
| [**IsLocked**](https://msdn.microsoft.com/en-us/library/Ee416377(v=VS.85).aspx)                                                   | Checks if the XAPO is locked.<br/>                                                                                                                                                |
| LONG m\_lReferenceCount<br/>                                                       | The XAPO object's COM reference count.<br/>                                                                                                                                       |
| [**ProcessThru**](https://msdn.microsoft.com/en-us/library/Ee416378(v=VS.85).aspx)                                             | Called by an [**IXAPO::Process**](https://msdn.microsoft.com/en-us/library/Ee418456(v=VS.85).aspx) implementation when an XAPO is disabled for thru processing.<br/>                                                  |
| [**ValidateFormatDefault**](https://msdn.microsoft.com/en-us/library/Ee416380(v=VS.85).aspx)                         | Verifies that an audio format falls within the default ranges supported.<br/>                                                                                                     |
| [**ValidateFormatPair**](https://msdn.microsoft.com/en-us/library/Ee416382(v=VS.85).aspx)                               | Verifies that an input and output format pair configuration is supported with respect to the XAPO property flags.<br/>                                                            |



 

## Related topics

<dl> <dt>

[**CXAPOBase class**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapobase)
</dt> </dl>

 

 




