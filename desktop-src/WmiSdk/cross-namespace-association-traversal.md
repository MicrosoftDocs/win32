---
description: Starting in Windows 7, Windows Management Instrumentation (WMI) implemented a standard mechanism for discovering profiles by using the CIM schema.
ms.assetid: e748b623-5ff3-464d-ba09-96cf226de7b6
ms.tgt_platform: multiple
title: Cross-Namespace Association Traversal
ms.topic: article
ms.date: 05/31/2018
---

# Cross-Namespace Association Traversal

Starting in Windows 7, Windows Management Instrumentation (WMI) implemented a standard mechanism for discovering profiles by using the CIM schema.

WMI supports the cross-namespace association traversal and association profile registration. For more information about profile registration and the CIM standard implementation of association traversal, see DSP1033 ([https://www.dmtf.org/standards/published\_documents/DSP1033.pdf](https://www.dmtf.org/sites/default/files/standards/documents/DSP1033_1.0.0.pdf))

To support this feature, the WMI infrastructure did the following:

-   Created the interop namespace: \\root\\interop.
-   Allowed cross namespace association traversal. Associations that cross namespaces support filtering at the association class level and at the implemented namespace level.
-   Added the [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)), [**CIM\_ElementConformsToProfile**](/previous-versions/windows/desktop/iscsitarg/cim-elementconformstoprofile), and [**CIM\_ReferencedProfile**](cim-referencedprofile.md) classes.
-   Implemented CIM Schema version 2.17.1 compatibility. For more information, see [CIM Schema Compatibility](cim-schema-compatibility.md).

## Interop Namespace

The interop namespace provides a common location for a client application to discover all of the profiles that are supported on a computer. Profiles can be used to manage various aspects of an operating system, storage array, or database.

All interop classes and objects must be defined in the root\\interop namespace.

## CIM Classes

The CIM classes described in the following list support cross-namespace association traversal.

<dl> <dt>

<span id="CIM_RegisteredProfile"></span><span id="cim_registeredprofile"></span><span id="CIM_REGISTEREDPROFILE"></span>[**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85))
</dt> <dd>

Used to identify the profile specification that is advertised as being implemented. This class specifies information that includes the profile name, organization, and version with which the implementation is compliant.

</dd> <dt>

<span id="CIM_ElementConformsToProfile"></span><span id="cim_elementconformstoprofile"></span><span id="CIM_ELEMENTCONFORMSTOPROFILE"></span>[**CIM\_ElementConformsToProfile**](/previous-versions/windows/desktop/iscsitarg/cim-elementconformstoprofile)
</dt> <dd>

Used to associate instances of management elements that are defined in profiles with the [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)) class that identifies the particular profile specifications that are implemented.

</dd> <dt>

<span id="CIM_ReferencedProfile"></span><span id="cim_referencedprofile"></span><span id="CIM_REFERENCEDPROFILE"></span>[**CIM\_ReferencedProfile**](cim-referencedprofile.md)
</dt> <dd>

Used to represent the relationship between profiles.

</dd> </dl>

## Implementing Cross-Namespace Association Traversal

The WMI service allows cross-namespace association traversal. WMI provides the interop namespace for registering profiles and associating them with profiles that are implemented in different namespaces. However, to use association traversal, implementers must instantiate the profile classes both in the interop and in the implemented namespace. For more information, see [Writing an Association Provider for Interop](writing-an-association-provider-for-interop.md).

Associations that cross namespaces within the same management environment must be instantiated in both the interop and implemented namespaces. Otherwise, association traversal will not work. For example, the power profile association provider must be registered with both root/interop and root/cimv2/power namespaces. Association traversal should be able to occur from either namespace back to the other. For examples of association traversal, see [Accessing Data in the Interop Namespace](accessing-data-in-the-interop-namespace.md).

**Windows Vista:  **

After upgrading to Windows 7, if there are interop device profiles that were previously installed in the root/interop namespace, no Windows 7 profiles will be installed. These third-party profile objects overwrite Windows 7 interop schema to maintain functionality. Additionally, the WMI application event ID 5631 is recorded.

To get the Windows 7 interop profiles, the Windows 7 version of the Interop.mof file and the related MFL files must be compiled. For more information, see [Compiling MOF Files](compiling-mof-files.md).

## Related topics

<dl> <dt>

[**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85))
</dt> <dt>

[**CIM\_ElementConformsToProfile**](/previous-versions/windows/desktop/iscsitarg/cim-elementconformstoprofile)
</dt> <dt>

[**CIM\_ReferencedProfile**](cim-referencedprofile.md)
</dt> <dt>

[CIM Schema Compatibility](cim-schema-compatibility.md)
</dt> <dt>

[Writing an Association Provider for Interop](writing-an-association-provider-for-interop.md)
</dt> <dt>

[Accessing Data in the Interop Namespace](accessing-data-in-the-interop-namespace.md)
</dt> </dl>

 

 
