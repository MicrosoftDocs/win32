---
Description: Shows the members of the CXAPOParametersBase class.
ms.assetid: C2113358-07DE-426E-AF26-BD8ED9902192
title: CXAPOParametersBase Members
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CXAPOParametersBase Members

Shows the members of the [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) class.

## Public Constructors



|                                                    |                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------|
| [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) | Constructs a [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) object. |



 

## Public Methods



|                                                                                                                              |                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddRef**](https://msdn.microsoft.com/library/Ee418448(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                         | Increments the XAPO object's reference count.<br/>                                                                                                         |
| [**BeginProcess**](https://msdn.microsoft.com/en-us/library/Ee416384(v=VS.85).aspx)                                                                     | Returns the current process parameters. <br/>                                                                                                              |
| [**CalcInputFrames**](https://msdn.microsoft.com/en-us/library/Ee418449(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                           | Returns the number of input frames required to generate the given number of output frames.<br/>                                                            |
| [**CalcOutputFrames**](https://msdn.microsoft.com/en-us/library/Ee418450(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                         | Returns the number of output frames required to generate the given number of input frames.<br/>                                                            |
| [**EndProcess**](https://msdn.microsoft.com/en-us/library/Ee416388(v=VS.85).aspx)                                                                         | Notifies [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) that the XAPO has finished accessing the current process parameters. <br/>                     |
| [**GetParameters**](https://msdn.microsoft.com/en-us/library/Ee418443(v=VS.85).aspx) (inherited from [**IXAPOParameters**](/windows/desktop/api/XAPO/nn-xapo-ixapoparameters)) | Gets effect-specific parameters. <br/>                                                                                                                     |
| [**GetRegistrationProperties**](https://msdn.microsoft.com/en-us/library/Ee418451(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))       | Returns the registration properties of an XAPO.<br/>                                                                                                       |
| [**Initialize**](https://msdn.microsoft.com/en-us/library/Ee418452(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                     | Performs any effect-specific initialization.<br/>                                                                                                          |
| [**IsInputFormatSupported**](https://msdn.microsoft.com/en-us/library/Ee418453(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))             | Queries if a specific input format is supported for a given output format.<br/>                                                                            |
| [**IsOutputFormatSupported**](https://msdn.microsoft.com/en-us/library/Ee418454(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))           | Queries if a specific output format is supported for a given input format.<br/>                                                                            |
| [**LockForProcess**](https://msdn.microsoft.com/en-us/library/Ee418455(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                             | Notifies XAPO of stream formats [**Process**](https://msdn.microsoft.com/en-us/library/Ee418456(v=VS.85).aspx) will be given.<br/>                                                             |
| [**OnSetParameters**](https://msdn.microsoft.com/en-us/library/Ee416390(v=VS.85).aspx)                                                               | Called by [**IXAPOParameters::SetParameters**](https://msdn.microsoft.com/en-us/library/Ee418447(v=VS.85).aspx) to allow for user-defined parameter validation. <br/>          |
| [**ParametersChanged**](https://msdn.microsoft.com/en-us/library/Ee416392(v=VS.85).aspx)                                                           | Indicates if [**IXAPOParameters::SetParameters**](https://msdn.microsoft.com/en-us/library/Ee418447(v=VS.85).aspx) has been called since the last processing pass. <br/>       |
| [**QueryInterface**](https://msdn.microsoft.com/library/Ee418457(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                         | Retrieves the requested interface pointer if the XAPO supports it.<br/>                                                                                    |
| [**Release**](https://msdn.microsoft.com/library/Ee418458(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                       | Decrements the XAPO object's reference count and deletes the object if the reference count falls to zero.<br/>                                             |
| [**Reset**](https://msdn.microsoft.com/en-us/library/Ee418459(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                               | Returns the object to the state it was in just after [**LockForProcess**](https://msdn.microsoft.com/en-us/library/Ee418455(v=VS.85).aspx) was called.<br/>                             |
| [**SetParameters**](https://msdn.microsoft.com/en-us/library/Ee418447(v=VS.85).aspx) (inherited from [**IXAPOParameters**](/windows/desktop/api/XAPO/nn-xapo-ixapoparameters)) | Sets effect-specific parameters.<br/>                                                                                                                      |
| [**UnlockForProcess**](https://msdn.microsoft.com/en-us/library/Ee418460(v=VS.85).aspx) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                         | Opposite of LockForProcess: variables allocated during [**LockForProcess**](https://msdn.microsoft.com/en-us/library/Ee418455(v=VS.85).aspx) should be deallocated in this method.<br/> |



 

## Related topics

<dl> <dt>

[**CXAPOParametersBase class**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase)
</dt> </dl>

 

 




