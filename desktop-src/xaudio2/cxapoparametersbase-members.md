---
description: Shows the members of the CXAPOParametersBase class.
ms.assetid: C2113358-07DE-426E-AF26-BD8ED9902192
title: CXAPOParametersBase Members
ms.topic: article
ms.date: 05/31/2018
---

# CXAPOParametersBase Members

Shows the members of the [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) class.

## Public Constructors



|    Constructor                                                |     Description                                                                    |
|----------------------------------------------------|-------------------------------------------------------------------------|
| [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) | Constructs a [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) object. |



 

## Public Methods



|        Method                                                                                                                      |     Description                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddRef**](/previous-versions/windows/desktop/legacy/ee418448(v=vs.85)) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                         | Increments the XAPO object's reference count.<br/>                                                                                                         |
| [**BeginProcess**](/windows/win32/api/xapobase/nf-xapobase-cxapoparametersbase-beginprocess)                                                                     | Returns the current process parameters. <br/>                                                                                                              |
| [**CalcInputFrames**](/windows/win32/api/xapo/nf-xapo-ixapo-calcinputframes) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                           | Returns the number of input frames required to generate the given number of output frames.<br/>                                                            |
| [**CalcOutputFrames**](/windows/win32/api/xapo/nf-xapo-ixapo-calcoutputframes) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                         | Returns the number of output frames required to generate the given number of input frames.<br/>                                                            |
| [**EndProcess**](/windows/win32/api/xapobase/nf-xapobase-cxapoparametersbase-endprocess)                                                                         | Notifies [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) that the XAPO has finished accessing the current process parameters. <br/>                     |
| [**GetParameters**](/windows/win32/api/xapo/nf-xapo-ixapoparameters-getparameters) (inherited from [**IXAPOParameters**](/windows/desktop/api/XAPO/nn-xapo-ixapoparameters)) | Gets effect-specific parameters. <br/>                                                                                                                     |
| [**GetRegistrationProperties**](/windows/win32/api/xapo/nf-xapo-ixapo-getregistrationproperties) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))       | Returns the registration properties of an XAPO.<br/>                                                                                                       |
| [**Initialize**](/windows/win32/api/xapo/nf-xapo-ixapo-initialize) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                     | Performs any effect-specific initialization.<br/>                                                                                                          |
| [**IsInputFormatSupported**](/windows/win32/api/xapo/nf-xapo-ixapo-isinputformatsupported) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))             | Queries if a specific input format is supported for a given output format.<br/>                                                                            |
| [**IsOutputFormatSupported**](/windows/win32/api/xapo/nf-xapo-ixapo-isoutputformatsupported) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))           | Queries if a specific output format is supported for a given input format.<br/>                                                                            |
| [**LockForProcess**](/windows/win32/api/xapo/nf-xapo-ixapo-lockforprocess) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                             | Notifies XAPO of stream formats [**Process**](/windows/win32/api/xapo/nf-xapo-ixapo-process) will be given.<br/>                                                             |
| [**OnSetParameters**](/windows/win32/api/xapobase/nf-xapobase-cxapoparametersbase-onsetparameters)                                                               | Called by [**IXAPOParameters::SetParameters**](/windows/win32/api/xapo/nf-xapo-ixapoparameters-setparameters) to allow for user-defined parameter validation. <br/>          |
| [**ParametersChanged**](/windows/win32/api/xapobase/nf-xapobase-cxapoparametersbase-parameterschanged)                                                           | Indicates if [**IXAPOParameters::SetParameters**](/windows/win32/api/xapo/nf-xapo-ixapoparameters-setparameters) has been called since the last processing pass. <br/>       |
| [**QueryInterface**](/previous-versions/windows/desktop/legacy/ee418457(v=vs.85)) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                         | Retrieves the requested interface pointer if the XAPO supports it.<br/>                                                                                    |
| [**Release**](/previous-versions/windows/desktop/legacy/ee418458(v=vs.85)) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                       | Decrements the XAPO object's reference count and deletes the object if the reference count falls to zero.<br/>                                             |
| [**Reset**](/windows/win32/api/xapo/nf-xapo-ixapo-reset) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                                               | Returns the object to the state it was in just after [**LockForProcess**](/windows/win32/api/xapo/nf-xapo-ixapo-lockforprocess) was called.<br/>                             |
| [**SetParameters**](/windows/win32/api/xapo/nf-xapo-ixapoparameters-setparameters) (inherited from [**IXAPOParameters**](/windows/desktop/api/XAPO/nn-xapo-ixapoparameters)) | Sets effect-specific parameters.<br/>                                                                                                                      |
| [**UnlockForProcess**](/windows/win32/api/xapo/nf-xapo-ixapo-unlockforprocess) (inherited from [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo))                         | Opposite of LockForProcess: variables allocated during [**LockForProcess**](/windows/win32/api/xapo/nf-xapo-ixapo-lockforprocess) should be deallocated in this method.<br/> |



 

## Related topics

<dl> <dt>

[**CXAPOParametersBase class**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase)
</dt> </dl>

 

 
