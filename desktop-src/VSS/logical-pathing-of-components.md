---
description: Logical pathing is used to organize components managed by a writer into well-defined groups.
ms.assetid: 663c8ca9-8f5b-48bd-af2d-b2d90de9e492
title: Logical Pathing of Components
ms.topic: article
ms.date: 05/31/2018
---

# Logical Pathing of Components

[*Logical pathing*](vssgloss-l.md) is used to organize components managed by a writer into well-defined groups.

The logical path is analogous in structure to traditional file pathing, using the backslash "\\" to separate elements in the path. Unlike file paths, the root of a logical path is **NULL**, instead of "\\".

The logical path is expressed as a **NULL**-terminated string, and there are no other restrictions on the characters the path can contain.

The most important use of logical pathing is in defining [*component sets*](vssgloss-c.md), where the [*explicit component inclusion*](vssgloss-e.md) in a backup or restore operation of one selectable component requires the inclusion of a number of other components ([*subcomponent*](vssgloss-s.md)). The logical path of the defining component of a component set is a parent to the logical paths of its subcomponents and:

-   Subcomponents must share as a root path the logical path of the selectable component that defines the component set.
-   A root path of **NULL** is valid.
-   The name of the defining selectable component must be the first logical path element after the root path for every nonselectable subcomponent of the component set.
-   Component sets can be nested.
-   The combination of logical path and component name must be unique across all instances of a [*writer class*](vssgloss-w.md).

The hypothetical example of a writer *MyWriter* with a logical path structure defined below illustrates logical pathing.



| Component name | Logical path            | Selectable for backup |
|----------------|-------------------------|-----------------------|
| "Executables"  | ""                      | N                     |
| "ConfigFiles"  | "Executables"           | N                     |
| "LicenseInfo"  | ""                      | Y                     |
| "Security"     | ""                      | Y                     |
| "UserInfo"     | "Security"              | N                     |
| "Certificates" | "Security"              | N                     |
| "writerData"   | ""                      | Y                     |
| "Set1"         | "writerData"            | N                     |
| "Jan"          | "writerData\\Set1"      | N                     |
| "Dec"          | "writerData\\Set1"      | N                     |
| "Set2"         | "writerData"            | N                     |
| "Jan"          | "writerData\\Set2"      | N                     |
| "Dec"          | "writerData\\Set2"      | N                     |
| "Query"        | "writerData\\QueryLogs" | N                     |
| "Usage"        | "writerData"            | Y                     |
| "Jan"          | "writerData\\Usage"     | N                     |
| "Dec"          | "writerData\\Usage"     | N                     |



 

Note that the components "Executables" and "ConfigFile" have a parent-child relationship, but both are nonselectable. Therefore, they do not form a component set. Whenever the writer *MyWriter* is backed up or restored, these two components will have to be [*explicitly included*](vssgloss-e.md) in the operation.

The component "LicenseInfo" is selectable with neither ancestor nor descendant. It can be explicitly included, or not, in a backup or restore operation at the discretion of the requester.

The component "Security" defines a simple component set, containing no component sets beneath it.

The component "writerData" defines a component set, which contains a complex collection of components with several well-defined logical path hierarchies beneath it.

One subcomponent, "Usage", is selectable and defines a component set.

Several components have the same name and are distinguished by their logical paths. Instances of the nonselectable components "Dec" and "Jan" exist under the components nonselectable components "Set1" and "Set2" and under the selectable subcomponent "Usage".

If the component "writerData" is explicitly included in a backup or restore, then all of its subcomponents—even those in the nested component set defined by "Usage"—will be [*implicitly included*](vssgloss-e.md)[*implicitly included*](vssgloss-i.md) in the operation.

If the component set defined by "writerData" is not explicitly included in a backup or restore, components "Set1", "Set2", and "QueryLogs" (and their instances of subcomponents "Dec" and "Jan") will not be included implicitly in the backup or restore operation.

However, even if "writerData" is not included in the operation, the component "Usage" is still selectable, and it can still be explicitly included in a backup or restore operation. If it is, then its subcomponents "Jan" and "Dec" will be implicitly included.

Other points worthy of note:

-   The selectable components "LicenseInfo" and "writerData" and the nonselectable component "Executables" are all at the same level in *MyWriter*'s logical path hierarchy: all have the same logical path of **NULL** or "", the root logical path.
-   The selectable component "Usage" should never be explicitly included in a backup, if its selectable parent ("writerData") is explicitly included in a backup or restore operation.
-   Components that define component sets may exist simply for organizational reasons. For instance, either the "writerData" or the "Usage" component, or both, might be empty; that is, no [*file sets*](vssgloss-f.md) were added to them using the [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup), [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles) or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles) method. The components still define a component set.

 

 



