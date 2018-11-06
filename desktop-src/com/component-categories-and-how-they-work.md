---
title: Component Categories and How they Work
description: Component Categories and How they Work
ms.assetid: efbf4a25-3c73-4d09-a172-6676c6d6501b
ms.topic: article
ms.date: 05/31/2018
---

# Component Categories and How they Work

Component categories identify those areas of functionality that a software component supports and requires, a registry entry is used for each category or identified area of functionality. Each component category is identified by a globally unique identifier (GUID), when a control is installed it registers itself as a control in the system registry using the component category ID for control, see [Self Registration for Controls](self-registration-for-controls.md). Within the controls self registration it will also register those component categories that it implements and those component categories that it requires a container to support in order to successfully host the control.

When a control container is offering controls to the user to insert, it only allows the user to select and instantiate those controls that will be able to function adequately in that environment. For example, if the control container does not support databinding, then the container will not allow the user to select and instantiate those controls that have an entry in the registry signifying that they require the databinding component category. A common dialog for control insertion and APIs to handle the registry entries are available.

Component categories are not cumulative or exclusive, a control can require any mix of component categories to function. A control that has no required entries for component categories may be expected to be capable of functioning in any control container and not require any specific functionality of a control container to function.

The following component categories are identified here, where necessary more detailed specifications of the categories may be available.

-   [**ISimpleFrameSite**](/windows/desktop/api/OCIdl/nn-ocidl-isimpleframesite) control containment.
-   Simple Databinding through the [**IPropertyNotifySink**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertynotifysink) interface.
-   Advanced Databinding (as supported by the additional databinding interfaces of VB4.0).
-   Visual Basic private interfaces - [**IVBFormat**](/windows/desktop/api/VbInterf/nn-vbinterf-ivbformat), [**IVBGetControl**](/windows/desktop/api/VbInterf/nn-vbinterf-ivbgetcontrol)
-   Internet aware controls.
-   Windowless controls.

This is not a definitive list of categories; further categories are likely to be defined in the future as new requirements are identified. An up-to-date list of component categories is available from Microsoft; this list reflects those component categories that have been identified by Microsoft and any others that about which vendors have informed Microsoft.

It is important to remember that controls should attempt to work in as many environments as possible. If it is possible, the control should degrade its functionality when placed in a container that does not support certain interfaces. The purpose of component categories is to prevent a situation where the control is placed in an environment that is unsuitable and the control cannot achieve its desired task. Generally, a control should degrade gracefully when interfaces are not present, a control may choose to advise the user with a message box that some functionality is not available or clearly document the functionality required of a control container for optimal performance.

Note older controls and containers do not make use of component categories and instead rely on the control keyword being present against the control in the registry. In order to be recognized by older containers controls may wish to register the control keyword in the registry, control developers should check that the control can successfully be hosted in such containers before doing this. Containers that use component categories may successfully use them to host older controls as the components category DLL handles the mapping, a separate category exists for older controls CATID\_ControlV1 so that a container may optionally exclude them if necessary.

As component categories are identified by GUIDs it is possible for containers that offer particular specific functionality to have their own category IDs, generated using a GUID generation tool. However this can possibly undermine the advantage of interoperability of controls and containers so it is preferred that wherever possible existing component categories be used. Vendors are encouraged to consult together when defining new component categories to ensure that they meet the common requirements of the marketplace, and follow the spirit of interoperability of ActiveX controls.

## Related topics

<dl> <dt>

[Component Categories](component-categories.md)
</dt> </dl>

 

 




