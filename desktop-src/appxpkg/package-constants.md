---
title: Package constants (AppModel.h)
description: Specifies how packages are to be processed.
ms.assetid: 72E565C3-6CFD-47E3-8BAC-17D6E86B99DA
topic_type:
- apiref
api_name:
- PACKAGE_APPLICATIONS_MAX_COUNT
- PACKAGE_APPLICATIONS_MIN_COUNT
- PACKAGE_FAMILY_MAX_RESOURCE_PACKAGES
- PACKAGE_FAMILY_MIN_RESOURCE_PACKAGES
- PACKAGE_FILTER_ALL_LOADED
- PACKAGE_FILTER_BUNDLE
- PACKAGE_FILTER_DIRECT
- PACKAGE_FILTER_DYNAMIC
- PACKAGE_FILTER_HEAD
- PACKAGE_FILTER_HOSTRUNTIME
- PACKAGE_FILTER_OPTIONAL
- PACKAGE_FILTER_RESOURCE
- PACKAGE_FILTER_STATIC
- PACKAGE_GRAPH_MAX_SIZE
- PACKAGE_GRAPH_MIN_SIZE
- PACKAGE_INFORMATION_BASIC
- PACKAGE_INFORMATION_FULL
- PACKAGE_MAX_DEPENDENCIES
- PACKAGE_MIN_DEPENDENCIES
- PACKAGE_PROPERTY_BUNDLE
- PACKAGE_PROPERTY_DEVELOPMENT_MODE
- PACKAGE_PROPERTY_DYNAMIC
- PACKAGE_PROPERTY_FRAMEWORK
- PACKAGE_PROPERTY_HOSTRUNTIME
- PACKAGE_PROPERTY_OPTIONAL
- PACKAGE_PROPERTY_RESOURCE
- PACKAGE_PROPERTY_STATIC
api_location:
- AppModel.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Package constants

Specifies how packages are to be processed.

| Constant/value | Description | 
|----------------|-------------|
| <span id="PACKAGE_APPLICATIONS_MAX_COUNT"></span><span id="package_applications_max_count"></span><dl><dt><strong>PACKAGE_APPLICATIONS_MAX_COUNT</strong></dt><dt>100</dt></dl> | The maximum number of apps in a package.<br /> | 
| <span id="PACKAGE_APPLICATIONS_MIN_COUNT"></span><span id="package_applications_min_count"></span><dl><dt><strong>PACKAGE_APPLICATIONS_MIN_COUNT</strong></dt><dt>0</dt></dl> | The minimum number of apps in a package.<br /> | 
| <span id="PACKAGE_FAMILY_MAX_RESOURCE_PACKAGES"></span><span id="package_family_max_resource_packages"></span><dl><dt><strong>PACKAGE_FAMILY_MAX_RESOURCE_PACKAGES</strong></dt><dt>512</dt></dl> | The maximum number of resource packages a package can have.<br /> | 
| <span id="PACKAGE_FAMILY_MIN_RESOURCE_PACKAGES"></span><span id="package_family_min_resource_packages"></span><dl><dt><strong>PACKAGE_FAMILY_MIN_RESOURCE_PACKAGES</strong></dt><dt>0</dt></dl> | The minimum number of resource packages a package can have.<br /> | 
| <span id="PACKAGE_FILTER_ALL_LOADED"></span><span id="package_filter_all_loaded"></span><dl><dt><strong>PACKAGE_FILTER_ALL_LOADED</strong></dt><dt>0x00000000</dt></dl> | Process all packages in the dependency graph.<br /> This is equivalent to <strong>PACKAGE_FILTER_HEAD</strong>, <strong>PACKAGE_FILTER_DIRECT</strong>.<br /><blockquote><b>Note</b><br /><strong>PACKAGE_FILTER_ALL_LOADED</strong> may be altered or unavailable for releases after Windows 8.1. Instead, use <strong>PACKAGE_FILTER_HEAD</strong>, <strong>PACKAGE_FILTER_DIRECT</strong>.</blockquote><br /> | 
| <span id="PACKAGE_FILTER_BUNDLE"></span><span id="package_filter_bundle"></span><dl><dt><strong>PACKAGE_FILTER_BUNDLE</strong></dt><dt>0x00000080</dt></dl> | Process bundle packages in the package graph.<br /> | 
| <span id="PACKAGE_FILTER_DIRECT"></span><span id="package_filter_direct"></span><dl><dt><strong>PACKAGE_FILTER_DIRECT</strong></dt><dt>0x00000020</dt></dl> | Process the directly dependent packages of the head (first) package in the dependency graph.<br /> | 
| **PACKAGE_FILTER_DYNAMIC**<br/>0x00100000 | Process packages dynamically added to the package graph. |
| <span id="PACKAGE_FILTER_HEAD"></span><span id="package_filter_head"></span><dl><dt><strong>PACKAGE_FILTER_HEAD</strong></dt><dt>0x00000010</dt></dl> | Process the first package in the dependency graph.<br /> | 
| **PACKAGE_FILTER_HOSTRUNTIME**<br/>0x00200000 | Process host runtime dependency packages added to the package graph. |
| <span id="PACKAGE_FILTER_OPTIONAL"></span><span id="package_filter_optional"></span><dl><dt><strong>PACKAGE_FILTER_OPTIONAL</strong></dt><dt>0x00020000</dt></dl> | Process bundle packages in the package graph.<br /> | 
| <span id="PACKAGE_FILTER_RESOURCE"></span><span id="package_filter_resource"></span><dl><dt><strong>PACKAGE_FILTER_RESOURCE</strong></dt><dt>0x00000040</dt></dl> | Process resource packages in the package graph.<br /> | 
| **PACKAGE_FILTER_STATIC**<br/>0x00080000 | Process packages statically added to the package graph. |
| <span id="PACKAGE_GRAPH_MAX_SIZE"></span><span id="package_graph_max_size"></span><dl><dt><strong>PACKAGE_GRAPH_MAX_SIZE</strong></dt><dt>(1 + PACKAGE_MAX_DEPENDENCIES + PACKAGE_FAMILY_MAX_RESOURCE_PACKAGES)</dt></dl> | The maximum size of a package graph.<br /> | 
| <span id="PACKAGE_GRAPH_MIN_SIZE"></span><span id="package_graph_min_size"></span><dl><dt><strong>PACKAGE_GRAPH_MIN_SIZE</strong></dt><dt>1</dt></dl> | The minimum size of a package graph.<br /> | 
| <span id="PACKAGE_INFORMATION_BASIC"></span><span id="package_information_basic"></span><dl><dt><strong>PACKAGE_INFORMATION_BASIC</strong></dt><dt>0x00000000</dt></dl> | Retrieve basic information.<br /> | 
| <span id="PACKAGE_INFORMATION_FULL"></span><span id="package_information_full"></span><dl><dt><strong>PACKAGE_INFORMATION_FULL</strong></dt><dt>0x00000100</dt></dl> | Retrieve full information.<br /> | 
| <span id="PACKAGE_MAX_DEPENDENCIES"></span><span id="package_max_dependencies"></span><dl><dt><strong>PACKAGE_MAX_DEPENDENCIES</strong></dt><dt>128</dt></dl> | The maximum number of packages a package depends on.<br /> | 
| <span id="PACKAGE_MIN_DEPENDENCIES"></span><span id="package_min_dependencies"></span><dl><dt><strong>PACKAGE_MIN_DEPENDENCIES</strong></dt><dt>0</dt></dl> | The minimum number of packages a package depends on.<br /> | 
| <span id="PACKAGE_PROPERTY_BUNDLE"></span><span id="package_property_bundle"></span><dl><dt><strong>PACKAGE_PROPERTY_BUNDLE</strong></dt><dt>0x00000004</dt></dl> | The package is a bundle package.<br /> | 
| <span id="PACKAGE_PROPERTY_DEVELOPMENT_MODE"></span><span id="package_property_development_mode"></span><dl><dt><strong>PACKAGE_PROPERTY_DEVELOPMENT_MODE</strong></dt><dt>0x00010000</dt></dl> | The package was registered with the <a href="/uwp/api/Windows.Management.Deployment.DeploymentOptions"><strong>DeploymentOptions</strong></a> enumeration.<br /> | 
| **PACKAGE_PROPERTY_DYNAMIC**<br/>0x00100000 | The package is a dynamic dependency. |
| <span id="PACKAGE_PROPERTY_FRAMEWORK"></span><span id="package_property_framework"></span><dl><dt><strong>PACKAGE_PROPERTY_FRAMEWORK</strong></dt><dt>0x00000001</dt></dl> | The package is a framework.<br /> | 
| **PACKAGE_PROPERTY_HOSTRUNTIME**<br/>0x00200000 | The package is a host runtime dependency. |
| <span id="PACKAGE_PROPERTY_OPTIONAL"></span><span id="package_property_optional"></span><dl><dt><strong>PACKAGE_PROPERTY_OPTIONAL</strong></dt><dt>0x00000008</dt></dl> | The package is an optional package.<br /> | 
| <span id="PACKAGE_PROPERTY_RESOURCE"></span><span id="package_property_resource"></span><dl><dt><strong>PACKAGE_PROPERTY_RESOURCE</strong></dt><dt>0x00000002</dt></dl> | The package is a resource package.<br /> |
| **PACKAGE_PROPERTY_STATIC**<br/>0x00080000 | The package is a static dependency. |

## Static and dynamic entries

A packaged app is launched with entries in its package graph; and that's the *static package graph*. Conversely, an unpackaged app is launched with an empty package graph.

The [Dynamic Dependency API](/windows/windows-app-sdk/api/win32/_dynamicdependency/) adds entries dynamically to a package graph; and that's the *dynamic package graph*.

If the *flags* passed to [**GetCurrentPackageInfo**](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackageinfo) or [**GetCurrentPackageInfo2**](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackageinfo2) doesn't contain **PACKAGE_FILTER_DYNAMIC**, then the function looks only at the static package graph. That's the same behavior as explicitly including **PACKAGE_FILTER_STATIC** in *flags*. In other words, for those functions and for compatibility reasons, you need to opt in to receiving dynamic packages.

[**GetCurrentPackageInfo3**](/windows/win32/appxpkg/appmodel/nf-appmodel-getcurrentpackageinfo3), on the other hand, is opt-out. If you don't specify **PACKAGE_FILTER_DYNAMIC** or **PACKAGE_FILTER_STATIC**, then that's equivalent to specifying both; so you get dynamic entries. To opt out, specify **PACKAGE_FILTER_STATIC** but not **PACKAGE_FILTER_DYNAMIC**.

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows 8 \[desktop apps only\] |
| Minimum supported server | Windows Server 2012 \[desktop apps only\] |
| Header | `AppModel.h` |

## See also

* [GetCurrentPackageInfo](/windows/win32/api/AppModel/nf-appmodel-getcurrentpackageinfo))
* [GetPackageInfo](/windows/win32/api/AppModel/nf-appmodel-getpackageinfo)
* [PackageIdFromFullName](/windows/win32/api/AppModel/nf-appmodel-packageidfromfullname)
