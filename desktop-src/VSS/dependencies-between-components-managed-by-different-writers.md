---
Description: 'There are situations where data from one writer depends on data managed by another writer. In these cases, you should back up or restore data from both writers.'
ms.assetid: '0413c289-74b7-4e83-a227-00bfb264e56e'
title: Dependencies between Components Managed by Different Writers
---

# Dependencies between Components Managed by Different Writers

There are situations where data from one writer depends on data managed by another writer. In these cases, you should back up or restore data from both writers.

VSS handles this problem through the notion of an explicit writer-component dependency and the [**IVssWMDependency**](ivsswmdependency.md) interface.

A writer adds one or more dependencies while creating the Writer Metadata Document using the [**IVssCreateWriterMetadata::AddComponentDependency**](ivsscreatewritermetadata-addcomponentdependency.md) method. The writer passes the method the name and logical path of the dependent component (which it manages), as well as the name and logical path and the [*writer class ID*](vssgloss-w.md#base-vssgloss-writer-class) (the GUID identifying the class) of the component upon which it depends.

Once established, this dependency informs the requester that during any backup or restore operation both the dependent component and the targets of its dependencies must participate.

A given component can have multiple dependencies, which requires that it and all its dependent targets participate in the backup and restore together.

The dependent component and/or the target(s) of its dependencies can be included either [*explicitly*](vssgloss-e.md#base-vssgloss-explicit-component-inclusion) or [*implicitly*](vssgloss-i.md#base-vssgloss-implicit-component-inclusion) in a backup or restore operations.

The explicit writer component dependency mechanism should not be used to create a dependency between two components on the same writer. The selection rules can supply the same functionality more efficiently without risk of circular dependencies.

As an example, [**IVssCreateWriterMetadata::AddComponentDependency**](ivsscreatewritermetadata-addcomponentdependency.md) could be used to define the dependency of the component writerData (with logical path "") of the writer MyWriter on component internetData (with a logical path of "Connections") of a writer named InternetConnector with a writer Class ID X. (While it is possible for multiple writers with the same class ID to be on the system simultaneously, confusion will be avoided because the combination of logical path and component name is unique on the system under VSS.)

A writer adds multiple dependencies to a given component simply by calling [**IVssCreateWriterMetadata::AddComponentDependency**](ivsscreatewritermetadata-addcomponentdependency.md) repeated with different components from different writers. The number of other components a given component depends on can be found by examining the **cDependencies** member of the [**VSS\_COMPONENTINFO**](vss-componentinfo.md) structure.

A writer or requester retrieves instances of the [**IVssWMDependency**](ivsswmdependency.md) interface with [**IVssWMComponent::GetDependency**](ivsswmcomponent-getdependency.md). The **IVssWMDependency** returns the component name, logical path, and class ID of the writer managing the component that is the target of the dependency.

The dependency mechanism does not prescribe any particular order of preference between the dependent component and the targets of its dependencies. As noted above, all a dependency indicates is that whenever a given component is either backed up or restored, the component or components it depends on must be backed up or restored as well. The exact implementation of dependency is at the discretion of the backup application.

For example, in the case above, the component writerData (logical path "") depends on component InternetConnector (logical path "Connections"). A requester is free to interpret this in either of the following ways:

-   If the dependent component, writerData, is selected (implicitly or explicitly) for backup or restore, the requester must select (either implicitly or explicitly) the target of its dependency, internetData
-   If the target of its dependency, internetData, is not selected for backup, then the dependent component, writerData, should not be selected.

However, when developing support for dependencies, requester developers should be aware that there is no way a writer can determine if one of its components is a target of a dependency.

## Declaring Remote Dependencies

A distributed application is an application that can be configured to use one or more computers at a time. Typically the application runs on one or more application server computers and communicates with (but may or may not actually run on) one or more database server computers. This configuration is sometimes referred to as a multi-system deployment. Often the same application can also be configured to run on a single computer that runs both an application server and a database server. Such a configuration is called a single-system deployment. In both configurations, the application server and database server each have their own independent VSS writers.

In a multi-system deployment, if a component managed by the application's writer depends on a remote component managed by the database server's writer, this is called a remote dependency. (A single-system deployment, in contrast, has only local dependencies.)

As an example of a multi-system deployment, consider an application server that uses a SQL Server database server as a data store. The application-specific data, which includes the web parts, web content files, and the IIS metabase, resides on one or more computers, called front-end web servers. The actual SQL data store, which includes the Config database and multiple Content databases, resides on one or more other computers, called back-end database servers. Each of the front-end web servers contains the same application-specific content and configuration. Each of the back-end database servers can host any of the Content databases or the Config database. The application software runs only on the front-end web servers, not on the database servers. In this configuration, the application's VSS writer has remote dependencies on the components managed by the SQL writer.

A writer can declare a remote dependency by calling the [**AddComponentDependency**](ivsscreatewritermetadata-addcomponentdependency.md) method, prepending "\\\\*RemoteComputerName*\\", where *RemoteComputerName* is the name of the computer where the remote component resides, to the logical path in the *wszOnLogicalPath* parameter. The value of *RemoteComputerName* can be an IP address or a computer name returned by the [**GetComputerNameEx**](base.getcomputernameex) function.

**Windows Server 2003:** A writer cannot declare remote dependencies until Windows Server 2003 with Service Pack 1 (SP1).

To identify a dependency, a requester calls the [**GetWriterId**](ivsswmdependency-getwriterid.md), [**GetLogicalPath**](ivsscomponent-getlogicalpath.md), and [**GetComponentName**](ivsswmdependency-getcomponentname.md) methods of the [**IVssWMDependency**](ivsswmdependency.md) interface. The requester must examine the component name that **GetComponentName** returns in the *pbstrComponentName* parameter. If the component name begins with "\\\\", the requester must assume that it specifies a remote dependency and that the first component following "\\\\" is the *RemoteComputerName* that was specified when the writer called [**AddComponentDependency**](ivsscreatewritermetadata-addcomponentdependency.md). If the component name does not begin with "\\\\", the requester should assume that it specifies a local dependency.

If there is a remote dependency, the requester must back up the remote component when it backs up the local component. To back up the remote component, the requester should have an agent on the remote computer and should initiate the backup on the remote computer.

## Structuring Remote Dependencies

It is important to understand that a dependency is not a component in and of itself. A component is necessary to hold the dependency.

The following examples show two ways to structure a set of dependencies.

``` syntax
Example 1:
    Writer 1
        Component A
            File A
            File B
            Dependency (SQL/MSDE Writer, Component X, "\")
            Dependency (SQL/MSDE Writer, Component Y, "\")

Example 2:
    Writer 2
        Component A
            File A
            File B
        Component B
            Dependency (SQL/MSDE Writer, Component X, "\")
            Dependency (SQL/MSDE Writer, Component Y, "\")
```

In example 1, the dependencies are held by Component A. Because only components can be selected, not individual files, structuring Component A's dependencies this way would require that the entire component, both the files and the dependencies, must always be backed up and restored together. They cannot be backed up or restored individually.

In example 2, separate components (Components A and B) hold each of the dependencies. In this case, the two components can be selected independently, and therefore backed up and restored independently. Structuring the dependencies this way gives a distributed application much more flexibility in managing its remote dependencies.

## Supporting Remote Dependencies

A requester can provide full or partial support for remote dependencies.

To provide full support, the requester should do the following at backup and restore time.

At backup time, the requester must start the backup on the front-end (local) computer, determine the dependencies that exist, and spool additional backup jobs to capture the back-end databases. The requester must wait until after the back-end backup jobs on the remote computer have completed before calling the [**IVssBackupComponents::SetBackupSucceeded**](ivssbackupcomponents-setbackupsucceeded.md) and [**IVssBackupComponents::BackupComplete**](ivssbackupcomponents-backupcomplete.md) methods. If the requester waits until the backup of back-end components is complete before calling **BackupComplete**, this will produce a more easily recoverable backup for a writer that implements additional enhancements—such as topology locking, for example—during the backup. The following procedure outlines what the requester should do:

1.  On the local computer, the requester calls the [**IVssBackupComponents::InitializeForBackup**](ivssbackupcomponents-initializeforbackup.md), [**IVssBackupComponents::GatherWriterMetadata**](ivssbackupcomponents-gatherwritermetadata.md), [**IVssBackupComponents::PrepareForBackup**](ivssbackupcomponents-prepareforbackup.md), and [**IVssBackupComponents::DoSnapshotSet**](ivssbackupcomponents-dosnapshotset.md) methods.
2.  After the local shadow copy is completed, but before the backup is completed, the requester spools additional backup jobs by sending a request to its agent on the remote computer.
3.  On the remote computer, the requester's agent performs the spooled backup sequence by calling [**InitializeForBackup**](ivssbackupcomponents-initializeforbackup.md), [**GatherWriterMetadata**](ivssbackupcomponents-gatherwritermetadata.md), [**PrepareForBackup**](ivssbackupcomponents-prepareforbackup.md), [**DoSnapshotSet**](ivssbackupcomponents-dosnapshotset.md), [**SetBackupSucceeded**](ivssbackupcomponents-setbackupsucceeded.md), and [**BackupComplete**](ivssbackupcomponents-backupcomplete.md).
4.  When the requester's agent has completed the spooled jobs on the remote computer, the requester completes the backup sequence by calling [**SetBackupSucceeded**](ivssbackupcomponents-setbackupsucceeded.md) and [**BackupComplete**](ivssbackupcomponents-backupcomplete.md).

At restore time, the requester must start the restore involving the front-end (local) computer, select the components and their dependencies to be restored, and then send the [**PreRestore**](ivssbackupcomponents-prerestore.md) event by calling the **IVssBackupComponents::PreRestore** method. The requester should then spool the back-end restore jobs on the remote computer and call the [**IVssBackupComponents::PostRestore**](ivssbackupcomponents-postrestore.md) method when the back-end restores are complete. This requirement gives the front-end writer more control over the restore experience and a better administrator user experience overall. Because the backups across each of the systems do not occur at the same point in time, the front-end writer will need to perform some cleanup of the back-end data. In the example application discussed in the preceding "Declaring Remote Dependencies", the writer should initiate a site remapping or reindexing after a restore of one of the back-end databases has completed. To do this, the writer must receive events on the front-end server. The following procedure outlines what the requester should do:

1.  On the local computer, the requester calls [**IVssBackupComponents::InitializeForRestore**](ivssbackupcomponents-initializeforrestore.md), [**GatherWriterMetadata**](ivssbackupcomponents-gatherwritermetadata.md), [**IVssBackupComponents::SetSelectedForRestore**](ivssbackupcomponents-setselectedforrestore.md) (or [**IVssBackupComponentsEx::SetSelectedForRestoreEx**](ivssbackupcomponentsex-setselectedforrestoreex.md)), and [**PreRestore**](ivssbackupcomponents-prerestore.md).
2.  After the [**PreRestore**](ivssbackupcomponents-prerestore.md) phase is completed, but before the [**PostRestore**](ivssbackupcomponents-postrestore.md) phase begins, the requester spools additional restore jobs by sending a request to its agent on the remote computer.
3.  On the remote computer, the requester's agent performs the spooled restore jobs by calling [**InitializeForRestore**](ivssbackupcomponents-initializeforrestore.md), [**GatherWriterMetadata**](ivssbackupcomponents-gatherwritermetadata.md), [**SetSelectedForRestore**](ivssbackupcomponents-setselectedforrestore.md), [**PreRestore**](ivssbackupcomponents-prerestore.md), [**SetFileRestoreStatus**](ivssbackupcomponents-setfilerestorestatus.md) (or [**SetSelectedForRestoreEx**](ivssbackupcomponentsex-setselectedforrestoreex.md)), and [**PostRestore**](ivssbackupcomponents-postrestore.md).
4.  When the requester's agent has completed the spooled jobs on the remote computer, the requester completes the restore sequence by calling [**IVssBackupComponents::SetFileRestoreStatus**](ivssbackupcomponents-setfilerestorestatus.md) and [**PostRestore**](ivssbackupcomponents-postrestore.md).

To provide partial support for remote dependencies, the requester must follow remote dependencies and include them as part of the backup, but the ordering of events on front-end and back-end systems as detailed in the previous two procedures would not be required. For a requester that implements only partial support, the requester should refer to the writer application's backup/restore documentation to understand what scenarios can be supported.

 

 



