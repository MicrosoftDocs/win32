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
| [**AddRef**](https://www.bing.com/search?q=**AddRef**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                         | Increments the XAPO object's reference count.<br/>                                                                                                         |
| [**BeginProcess**](https://www.bing.com/search?q=**BeginProcess**)                                                                     | Returns the current process parameters. <br/>                                                                                                              |
| [**CalcInputFrames**](https://www.bing.com/search?q=**CalcInputFrames**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                           | Returns the number of input frames required to generate the given number of output frames.<br/>                                                            |
| [**CalcOutputFrames**](https://www.bing.com/search?q=**CalcOutputFrames**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                         | Returns the number of output frames required to generate the given number of input frames.<br/>                                                            |
| [**EndProcess**](https://www.bing.com/search?q=**EndProcess**)                                                                         | Notifies [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) that the XAPO has finished accessing the current process parameters. <br/>                     |
| [**GetParameters**](https://www.bing.com/search?q=**GetParameters**) (inherited from [**IXAPOParameters**](/windows/desktop/api/XAPO/nn-xapo-ixapoparameters)) | Gets effect-specific parameters. <br/>                                                                                                                     |
| [**GetRegistrationProperties**](https://www.bing.com/search?q=**GetRegistrationProperties**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))       | Returns the registration properties of an XAPO.<br/>                                                                                                       |
| [**Initialize**](https://www.bing.com/search?q=**Initialize**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                     | Performs any effect-specific initialization.<br/>                                                                                                          |
| [**IsInputFormatSupported**](https://www.bing.com/search?q=**IsInputFormatSupported**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))             | Queries if a specific input format is supported for a given output format.<br/>                                                                            |
| [**IsOutputFormatSupported**](https://www.bing.com/search?q=**IsOutputFormatSupported**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))           | Queries if a specific output format is supported for a given input format.<br/>                                                                            |
| [**LockForProcess**](https://www.bing.com/search?q=**LockForProcess**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                             | Notifies XAPO of stream formats [**Process**](https://www.bing.com/search?q=**Process**) will be given.<br/>                                                             |
| [**OnSetParameters**](https://www.bing.com/search?q=**OnSetParameters**)                                                               | Called by [**IXAPOParameters::SetParameters**](https://www.bing.com/search?q=**IXAPOParameters::SetParameters**) to allow for user-defined parameter validation. <br/>          |
| [**ParametersChanged**](https://www.bing.com/search?q=**ParametersChanged**)                                                           | Indicates if [**IXAPOParameters::SetParameters**](https://www.bing.com/search?q=**IXAPOParameters::SetParameters**) has been called since the last processing pass. <br/>       |
| [**QueryInterface**](https://www.bing.com/search?q=**QueryInterface**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                         | Retrieves the requested interface pointer if the XAPO supports it.<br/>                                                                                    |
| [**Release**](https://www.bing.com/search?q=**Release**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                       | Decrements the XAPO object's reference count and deletes the object if the reference count falls to zero.<br/>                                             |
| [**Reset**](https://www.bing.com/search?q=**Reset**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                               | Returns the object to the state it was in just after [**LockForProcess**](https://www.bing.com/search?q=**LockForProcess**) was called.<br/>                             |
| [**SetParameters**](https://www.bing.com/search?q=**SetParameters**) (inherited from [**IXAPOParameters**](/windows/desktop/api/XAPO/nn-xapo-ixapoparameters)) | Sets effect-specific parameters.<br/>                                                                                                                      |
| [**UnlockForProcess**](https://www.bing.com/search?q=**UnlockForProcess**) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                         | Opposite of LockForProcess: variables allocated during [**LockForProcess**](https://www.bing.com/search?q=**LockForProcess**) should be deallocated in this method.<br/> |



 

## Related topics

<dl> <dt>

[**CXAPOParametersBase class**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase)
</dt> </dl>

 

 




