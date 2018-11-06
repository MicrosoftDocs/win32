---
title: Control Properties
description: Control Properties
ms.assetid: 29c2cca3-9460-45d1-9591-026e8c18f26f
ms.topic: article
ms.date: 05/31/2018
---

# Control Properties

In addition to properties defined and implemented by the control itself, ActiveX controls technology also involves:

<dl> <dt>

<span id="Ambient_properties"></span><span id="ambient_properties"></span><span id="AMBIENT_PROPERTIES"></span>Ambient properties
</dt> <dd>

These are exposed by the container through a control client site to provide environmental values that apply to all controls embedded in the container. For example, a container can provide a default background color or a default font that the control can use. Ambient properties are exposed through **IDispatch** implemented on a container's site object. The container calls the control's [**IOleControl::OnAmbientPropertyChange**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-onambientpropertychange) method when any of its ambient properties change value. In response, a control may need to update its own internal or visual state in response. The container indicates which ambient property changed with the DISPID parameter or may pass DISPID\_UNKNOWN to indicate that multiple ambient properties changed.

</dd> <dt>

<span id="Extended_properties"></span><span id="extended_properties"></span><span id="EXTENDED_PROPERTIES"></span>Extended properties
</dt> <dd>

These are actually implemented by a container to wrap the controls it contains to provide container-managed properties that appear as if they were native control properties. The container can aggregate the control, adding the extended properties to supplement or override the control's properties. The aggregated object is called an extended control. To the container, the extended control appears as the control itself and extended properties appear to be exposed by the control. The container supports an extended control through its client site method [**IOleControlSite::GetExtendedControl**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrolsite-getextendedcontrol). The **GetExtendedControl** method allows controls to navigate through the site to the extended control object provided for them by the container, if the container supports this feature. A container can also choose to show property pages for its extended controls in addition to those pages that a control would normally specify through [**ISpecifyPropertyPages**](/windows/desktop/api/OCIdl/nn-ocidl-ispecifypropertypages). Because of this, a control has to ask a container to show a property frame before the control attempts to do so itself. The control calls [**IOleControlSite::ShowPropertyFrame**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrolsite-showpropertyframe) to do this. If the container implements this function then it shows the property frame itself; if the method returns an error then the control can show the property frame.

</dd> </dl>

For more information, see the following topics:

-   [Standard Properties](standard-properties.md)
-   [Standard Font Object](standard-font-object.md)
-   [Standard Picture Object](standard-picture-object.md)

## Related topics

<dl> <dt>

[Control Methods](control-methods.md)
</dt> </dl>

 

 




