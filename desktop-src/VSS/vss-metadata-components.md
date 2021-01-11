---
description: Critical to organizing which files of which writer are to be backed up or restored is the concept of a component.
ms.assetid: 5f85bd0e-31bb-45aa-af7c-15299ed31b26
title: VSS Metadata Components
ms.topic: article
ms.date: 05/31/2018
---

# VSS Metadata Components

Critical to organizing which files of which writer are to be backed up or restored is the concept of a [*component*](vssgloss-c.md).

Components allow a writer to indicate to a backup engine how its files are to be organized, dependencies between files, and what type of data those files can contain. This allows a backup engine to decide how to store files for maximum efficiency.

In addition, VSS-based applications use components as the building blocks for their metadata and the medium for writer/requester communication.

Writers and requesters store information about components separately—in the Writer Metadata Document and the Backup Components Document, respectively—and the information differs in each representation.

Component information in Writer Metadata Documents includes the following:

-   Information from only one writer in each document
-   All of that writer's components, whether they can be [*explicitly included*](vssgloss-e.md) or must be [*implicitly included*](vssgloss-i.md) in a backup or restore operation
-   [*Logical path*](vssgloss-l.md) information used to associate a selectable for backup component with particular nonselectable for backup components, thus forming a component set
-   The [*file set*](vssgloss-f.md) information—path, file specification, and recursion flag—managed for each component

Writer Metadata Documents also contain writer-level metadata information, such as restore methods and alternate location mappings for restore. Writer Metadata Documents are read-only. The interface for examining this information is [**IVssWMComponent**](/windows/desktop/api/VsBackup/nl-vsbackup-ivsswmcomponent).

Component information in Backup Components Documents includes the following:

-   Only information on explicitly included components
-   Writer-level metadata information, such as alternate location mappings and restore
-   State information describing a backup or restore operation

Backup Component Documents do not contain information on components' [*file sets*](vssgloss-f.md). Backup Component Documents are not read-only and can be modified by the writer. The interface for accessing this information is [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent).

The life cycle and relationship between the two expressions of a component can be understood as follows:

-   Writers are responsible for the initial definitions of components.
-   A requester examines the metadata of all writers and their components.
-   From components' selectability and logical path information, a requester determines which components must be explicitly included, which may be explicitly included, which define component sets, and which are members of component sets.
-   A requester adds those components that require explicit inclusion, and implicitly includes subcomponents in [*component sets*](/windows) (whose information is not in the Backup Components Document).
-   When handling events, writers and requesters may modify and examine the component information stored in the Backup Components Document to coordinate their activity.

Both the writer and the requester versions component information are required to properly execute backup and restore operations, and both must be stored with any backed-up data:

-   [Component Types](component-types.md)
-   [Definition of Components by Writers](definition-of-components-by-writers.md)
-   [Use of Components by the Requester](use-of-components-by-the-requestor.md)

 

 
