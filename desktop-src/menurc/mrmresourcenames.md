---
title: Resource names in MRM
description: Description of resource names in MRM.
keywords:
- MrmIndexString MrmIndexFile MrmIndexEmbeddedData Menus and Other Resources
ms.topic: reference
---

# Resource names in MRM

Every resource in MRM has a name. Resource names are URIs conforming to [IETF RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986).

A resource name in MRM is of the following form:

    ms-resource://<PackageFamilyName>/<Root>/<Rest...>

Where:

* `ms-resource` is the **scheme**.
* `<PackageFamilyName>` is the **authority** and is either the Package Family Name of the app that will
use the resources, or the literal string `"Application"` for unpackaged apps.
* `<Root>` is a single **path segment**.
* `<Rest...>` is one or more other **path segments** separated by slashes.

The **query** and **fragment** portions of a URI are not allowed.

For brevity, this documentation typically refers to resource names without the scheme or authority
(for example "strings/foo" or just "foo").

### Case sensitivity

Although the scheme `ms-resource` is case-sensitive, the paths are not. 

All the following are equal:

    ms-resource:///FILES/LOGO.PNG
    ms-resource:///files/logo.png
    ms-resource:///FiLeS/LoGo.PnG

But the following are both errors:

    MS-RESOURCE:///files/logo.png
    Ms-Resource:///files.logo.png

If different resource candidates use different casings, the one that appears in the PRI file
is implementation-dependent. This does not matter, since runtime resource lookup is also 
case-insensitive.

### Authority

For convenience, MRM allows resource URIs to omit the `<PackageFamilyName>` when adding resource
to an indexer. Additionally, MRM allows specifying *any* valid **authority** as the `<PackageFamilyName>`
but it will be replaced with the value specified as *packageFamilyName* when creating
the resource indexer (see [**MrmCreateResourceIndexer**](mrmcreateresourceindexer.md) for
more info).

For example, assuming the resource indexer was created with the *packageFamilyName* of `"MyApp"`
then all of the following resource URIs are equivalent:

    ms-resource://MyApp/strings/foo     // Canonical form.
    ms-resource:///strings/foo          // Omit the PFN.
    ms-resource://App2/strings/foo      // PFN "App2" is ignored.

### Path

As indicated by the simplified grammar above, all resource names in MRM must have at least
two path segments, `<Root>` and `<Rest...>`. It is an error to have a single path segment in 
the resource name, or to end the resource name with a slash. The following are errors:

    ms-resource///hello                 // Error, only one path segment
    ms-resource///strings/hello/        // Error, ends with a slash

There is no practical limit to the number of path segments you can have, other than limits
on the total length of a URI (typically around 2,000 characters). All of the following
are valid resource names:

    ms-resource:///strings/hello
    ms-resource:///files/assets/logo.png
    ms-resource:///food/baked/muffins/lemon.and.blueberry/gluten_free

### Conventions

Although by no means required, the following conventions are used in PRI files.

* String resources are added to the "strings" `<RootPath>`.
* File resources are added to the "files" `<RootPath>`.
* Container resoures (e.g. resources from a `resw` file) are added to the "resources" `<RootPath>`.

Note that XAML localization depends on the "resources" convention (see [x:Uid directive](/windows/uwp/xaml-platform/x-uid-directive) for more info), and other libraries may depend on these conventions, too.

### Naming resources for libraries

When building PRI files to be part of a re-distributable library, it is important to choose
resource names that are unlikely to conflict with the names of the parent app (or other libraries).
This is because all the resources for an app (including resources for dependent libraries) are
merged into a single PRI file at build time - see [**MrmIndexResourceContainerAutoQualifiers**](mrmindexresourcecontainerautoqualifiers.md) for more info. If the same resource name is used by 
the main app and one of its libraries (or by two libraries) then an error will occur when generating 
the PRI.

To avoid this, consider namespacing your resources into a path that includes a unique 
segment, such as your company's reverse DNS name or a GUID.
