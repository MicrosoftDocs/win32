---
title: Required Interfaces
description: Required Interfaces
ms.assetid: 'ae238882-d0c9-4120-b8a8-001bf9559cfa'
---

# Required Interfaces

The table below lists the ActiveX Control Container interfaces, and denotes which interfaces are optional, and which are mandatory and must be implemented by control containers.



| Interface                                                                      | Required?      | Comments                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOleClientSite**](ioleclientsite.md)<br/>                            | Yes<br/> |                                                                                                                                                                                                                                                                                                                                                              |
| [**IAdviseSink**](iadvisesink.md)<br/>                                  | No<br/>  | Only when the container desires (a) data change notifications (controls with [**IDataObject**](idataobject.md)), (b) view change notification (controls that are not active and have [**IViewObject**](iviewobject.md) or [**IViewObject2**](iviewobject2.md)), and (c) other notifications from controls acting as standard embedded objects.<br/> |
| [**IOleInPlaceSite**](ioleinplacesite.md)<br/>                          | Yes<br/> |                                                                                                                                                                                                                                                                                                                                                              |
| [**IOleControlSite**](iolecontrolsite.md)<br/>                          | Yes<br/> |                                                                                                                                                                                                                                                                                                                                                              |
| [**IOleInPlaceFrame**](ioleinplaceframe.md)<br/>                        | Yes<br/> |                                                                                                                                                                                                                                                                                                                                                              |
| [**IOleContainer**](iolecontainer.md)<br/>                              | Yes<br/> | See note 1<br/>                                                                                                                                                                                                                                                                                                                                        |
| **IDispatch** for ambient properties<br/>                                | Yes<br/> | See note 2 and [Ambient Properties for Controls](ambient-properties-for-controls.md)<br/>                                                                                                                                                                                                                                                             |
| Control Event Sets<br/>                                                  | Yes<br/> | See note 2<br/>                                                                                                                                                                                                                                                                                                                                        |
| [**ISimpleFrameSite**](isimpleframesite.md)<br/>                        | No<br/>  | [**ISimpleFrameSite**](isimpleframesite.md) and support for nested simple frames is optional.<br/>                                                                                                                                                                                                                                                    |
| [IPropertyNotifySink](data-binding-through-ipropertynotifysink.md)<br/> | No<br/>  | Only needed for containers that (a) have their own property editing UI which would require updating whenever a control changed a property itself or (b) want to control \[[**requestedit**](https://msdn.microsoft.com/library/windows/desktop/aa367155)\] property changes and other such data-binding features.<br/>                                                                            |
| [IErrorInfo](http://go.microsoft.com/fwlink/p/?linkid=138948)<br/>       | Yes<br/> | Mandatory if container supports dual interfaces. See note 2.<br/>                                                                                                                                                                                                                                                                                      |
| [**IClassFactory2**](iclassfactory2.md)<br/>                            | No<br/>  | Support is strongly recommended.<br/>                                                                                                                                                                                                                                                                                                                  |



 

1.  [**IOleContainer**](iolecontainer.md) is implemented on the document or form object (or appropriate analog) that holds the container sites. Controls use **IOleContainer** to navigate to other controls in the same document or form.
2.  Support for dual interfaces is not mandatory, but is strongly recommended. Writing ActiveX control containers to take advantage of dual interfaces will afford better performance with controls that offer dual interface support.

ActiveX control containers must support OLE Automation exceptions. If a control container supports dual interfaces, then it must capture automation exceptions through [IErrorInfo](http://go.microsoft.com/fwlink/p/?linkid=138948).

## Related topics

<dl> <dt>

[Containers](containers.md)
</dt> </dl>

 

 





