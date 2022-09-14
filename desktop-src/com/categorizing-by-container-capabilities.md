---
title: Categorizing by Container Capabilities
description: Components often require certain functionality from the container and will not work with a container that does not provide the support.
ms.assetid: 11002f3e-17de-4e05-a2df-0c9e6326846d
ms.topic: article
ms.date: 05/31/2018
---

# Categorizing by Container Capabilities

Components often require certain functionality from the container and will not work with a container that does not provide the support. The user interface should filter out components that require functionality the container does not support. To accomplish this, components can be categorized by the required container functionality.

An example of components that require functionality from the container and do not work in containers that do not support that functionality are simple frame OLE controls. Categorizing by container capabilities is accomplished by an additional registry key within the component's CLSID key:

``` syntax
;The CLSID for "Simple Frame Control" is {123456FF-ABCD-4321-0101-00000000000C}HKEY_CASSES_ROOT\CLSID\{12346FF-ABCD-4321-0101-00000000000C}\Implemented Categories
;The CATID for "Control" is {40FC6ED4-2438-11cf-A3DB-080036F12502} HKEY_CLASSES_ROOT\CLSID\{123456FF-ABCD-4321-0101-00000000000C}Implemented Categories\{40FC6ED4-2438-11cf-A3DB-080036F12502}
;The CATID for simple frame controls is {...CATID_SimpleFrameControl...} HKEY_CLASSES_ROOT\CLSID\{123456FF-ABCD-4321-0101-00000000000C}Implemented Categories\{...CATID_SimpleFrameControl...}
HKEY_CLASSES_ROOT\CLSID\{123456FF-ABCD-4321-0101-00000000000C}Required Categories\{...CATID_SimpleFrameControl...}
 
```

As shown in this example, a component can belong to component categories that indicate supported functionality as well as to component categories that indicate required functionality.

In the following example, the button control is a generic OLE control that supports no additional functionality. It will work in any OLE control container.

``` syntax
HKEY_CLASSES_ROOT\CLSID\{...CLSID_Button...}\Implemented Categories
HKEY_CLASSES_ROOT\CLSID\{...CLSID_Button...}\Implemented Categories\{...CATID_Control...}
 
```

Compare the preceding example with the next example in which the MyDBControl can use Visual Basic data binding if the container supports it. However, it has been defined so that it will work in containers that do not support Visual Basic data binding (perhaps by a different database API):

``` syntax
HKEY_CLASSES_ROOT\CLSID\{...CLSID_MyDBControl...}\Implemented Categories
HKEY_CLASSES_ROOT\CLSID\{...CLSID_MyDBControl...}\Implemented Categories\{...CATID_Control...}
HKEY_CLASSES_ROOT\CLSID\{...CLSID_MyDBControl...}\Implemented Categories\{...CATID_VBDatabound...}
 
```

The GroupBox control is a simple frame control. It relies on the container implementing the [**ISimpleFrameSite**](/windows/desktop/api/OCIdl/nn-ocidl-isimpleframesite) interface and will work correctly only in such containers:

``` syntax
HKEY_CLASSES_ROOT\CLSID\{...CLSID_GroupBox...}\Implemented Categories
HKEY_CLASSES_ROOT\CLSID\{...CLSID_GroupBox...}\Implemented Categories\{...CATID_Control...}
HKEY_CLASSES_ROOT\CLSID\{...CLSID_GroupBox...}\Implemented Categories\{...CATID_SimpleFrame...}
HKEY_CLASSES_ROOT\CLSID\{...CLSID_GroupBox...}\Required Categories\{...CATID_SimpleFrame...}
 
```

A container that supports Visual Basic data bound controls but does not support simple frame controls would specify CATID\_Control and CATID\_VBDatabound to the insert control user interface. The list of controls displayed to the user would contain the CLSID\_Button and CLSID\_MyDBControl. CLSID\_GroupBox would not be displayed.

## Related topics

<dl> <dt>

[Associating Icons with a Category](associating-icons-with-a-category.md)
</dt> <dt>

[Categorizing by Component Capabilities](categorizing-by-component-capabilities.md)
</dt> <dt>

[Default Classes and Associations](default-classes-and-associations.md)
</dt> <dt>

[Defining Component Categories](defining-component-categories.md)
</dt> <dt>

[The Component Categories Manager](the-component-categories-manager.md)
</dt> </dl>

 

 




