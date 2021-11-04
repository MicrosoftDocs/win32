---
title: Required Interfaces (COM)
description: Learn about the ActiveX Control Container interfaces that can or must be implemented by control containers.
ms.assetid: ae238882-d0c9-4120-b8a8-001bf9559cfa
ms.topic: article
ms.date: 05/31/2018
---

# Required Interfaces (COM)

The table below lists the ActiveX Control Container interfaces, and denotes which interfaces are optional, and which are mandatory and must be implemented by control containers.



| Interface                                                                      | Required?      | Comments                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOleClientSite**](/windows/desktop/api/OleIdl/nn-oleidl-ioleclientsite)<br/>                            | Yes<br/> |                                                                                                                                                                                                                                                                                                                                                              |
| [**IAdviseSink**](/windows/desktop/api/ObjIdl/nn-objidl-iadvisesink)<br/>                                  | No<br/>  | Only when the container desires (a) data change notifications (controls with [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject)), (b) view change notification (controls that are not active and have [**IViewObject**](/windows/desktop/api/OleIdl/nn-oleidl-iviewobject) or [**IViewObject2**](/windows/desktop/api/OleIdl/nn-oleidl-iviewobject2)), and (c) other notifications from controls acting as standard embedded objects.<br/> |
| [**IOleInPlaceSite**](/windows/desktop/api/OleIdl/nn-oleidl-ioleinplacesite)<br/>                          | Yes<br/> |                                                                                                                                                                                                                                                                                                                                                              |
| [**IOleControlSite**](/windows/desktop/api/OCIdl/nn-ocidl-iolecontrolsite)<br/>                          | Yes<br/> |                                                                                                                                                                                                                                                                                                                                                              |
| [**IOleInPlaceFrame**](/windows/desktop/api/OleIdl/nn-oleidl-ioleinplaceframe)<br/>                        | Yes<br/> |                                                                                                                                                                                                                                                                                                                                                              |
| [**IOleContainer**](/windows/desktop/api/OleIdl/nn-oleidl-iolecontainer)<br/>                              | Yes<br/> | See note 1<br/>                                                                                                                                                                                                                                                                                                                                        |
| **IDispatch** for ambient properties<br/>                                | Yes<br/> | See note 2 and [Ambient Properties for Controls](ambient-properties-for-controls.md)<br/>                                                                                                                                                                                                                                                             |
| Control Event Sets<br/>                                                  | Yes<br/> | See note 2<br/>                                                                                                                                                                                                                                                                                                                                        |
| [**ISimpleFrameSite**](/windows/desktop/api/OCIdl/nn-ocidl-isimpleframesite)<br/>                        | No<br/>  | [**ISimpleFrameSite**](/windows/desktop/api/OCIdl/nn-ocidl-isimpleframesite) and support for nested simple frames is optional.<br/>                                                                                                                                                                                                                                                    |
| [IPropertyNotifySink](data-binding-through-ipropertynotifysink.md)<br/> | No<br/>  | Only needed for containers that (a) have their own property editing UI which would require updating whenever a control changed a property itself or (b) want to control \[[**requestedit**](/windows/desktop/Midl/requestedit)\] property changes and other such data-binding features.<br/>                                                                            |
| [IErrorInfo](/windows/win32/api/oaidl/nn-oaidl-ierrorinfo)<br/>       | Yes<br/> | Mandatory if container supports dual interfaces. See note 2.<br/>                                                                                                                                                                                                                                                                                      |
| [**IClassFactory2**](/windows/desktop/api/OCIdl/nn-ocidl-iclassfactory2)<br/>                            | No<br/>  | Support is strongly recommended.<br/>                                                                                                                                                                                                                                                                                                                  |



 

1.  [**IOleContainer**](/windows/desktop/api/OleIdl/nn-oleidl-iolecontainer) is implemented on the document or form object (or appropriate analog) that holds the container sites. Controls use **IOleContainer** to navigate to other controls in the same document or form.
2.  Support for dual interfaces is not mandatory, but is strongly recommended. Writing ActiveX control containers to take advantage of dual interfaces will afford better performance with controls that offer dual interface support.

ActiveX control containers must support OLE Automation exceptions. If a control container supports dual interfaces, then it must capture automation exceptions through [IErrorInfo](/windows/win32/api/oaidl/nn-oaidl-ierrorinfo).

## Related topics

<dl> <dt>

[Containers](containers.md)
</dt> </dl>

 

