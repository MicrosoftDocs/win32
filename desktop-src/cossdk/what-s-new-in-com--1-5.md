---
description: COM+ version 1.5 adds new features that are designed to increase the overall scalability, availability, and manageability of COM+ applications both for developers and for system administrators.
ms.assetid: e7073ba5-6b19-4d94-8cc0-b4e16bb44afd
title: Whats New in COM+ 1.5
ms.topic: article
ms.date: 05/31/2018
---

# What's New in COM+ 1.5

COM+ version 1.5 adds new features that are designed to increase the overall scalability, availability, and manageability of COM+ applications both for developers and for system administrators.

COM+ 1.5 is available starting with Windows XP and Windows Server 2003. The new COM+ 1.5 features are not available in Windows 2000.

## Application-Level Access Checks Enabled by Default

As part of the enhanced security of the system, access checks are enabled by default when creating a COM+ application. In previous versions, access checks were disabled by default at the application level and enabled by default at the component level. Starting with Windows Server 2003, access checks are enabled by default at the application level and disabled by default at the component level. See [Creating a New COM+ Application](creating-a-new-com--application.md), [Enabling Access Checks for an Application](enabling-access-checks-for-an-application.md), and [Enabling Access Checks at the Component Level](enabling-access-checks-at-the-component-level.md) for more information and procedures on how to change the default settings.

## Application Pooling

With the new ConcurrentApps property of the [**COMAdminCatalogObject**](comadmincatalogobject.md) object in the [**Applications**](applications.md) collection, COM+ Application Pooling adds scalability for single-threaded processes and integrates with the new COM+ Application Recycling service. See [COM+ Application Pooling](com--application-pooling.md) for detailed information.

## Application Recycling

Application recycling significantly increases the overall stability of your applications. Because the performance of most applications can degrade over time due to factors such as memory leaks, reliance on third-party code, and nonscalable resource usage, COM+ application recycling provides a simple solution to gracefully shut down a process associated with an application and restart it. See [COM+ Application Recycling](com--application-recycling.md) for detailed information. Also see "Configuring Process Recycling" in the Component Services Administration Help for a step-by-step procedure for configuring process recycling.

## COM+ Partitions

In this release, COM+ introduces support for COM+ partitions, a feature that allows multiple versions of COM+ applications to be installed and configured on the same machine. This feature can save you the cost and time-consuming effort of using multiple servers to manage different versions of an application. On a single machine, each partition acts, in effect, as a virtual server. After installing the application into each partition, you create partition sets that map users to the logical servers. See [COM+ Partitions](com--partitions.md) for detailed information about how to set up and manage COM+ partitions. Also see "Administering Application Partitions" in the Component Services Administration Help for step-by-step procedures.

## COM+ Services Without Components

With COM+ 1.5, you can use the services provided by COM+ without needing to build a component to contain the methods that call those services. This greatly benefits developers who do not normally use components but want to use COM+ services such as transactions or the COM+ Tracker. By using COM+ services without components, developers can avoid the overhead of creating a component that is used to access only the COM+ services they need. See [COM+ Services Without Components](com--services-without-components.md) for detailed information.

## COM+ SOAP Service

With COM+ 1.5, you can now expose a COM+ application as an XML web service. You can also transparently use an XML web service, whether deployed using COM+ or not, as a COM component. This means that you can easily create new XML web services out of existing COM+ applications and easily incorporate XML web services into new COM+ applications. See [COM+ SOAP Service](com--soap-service.md) for detailed information.

## Configurable Isolation Levels

COM+ developers can use the new TxIsolationLevel property or the Component Services administrative tool to configure an application's isolation level according to need, helping to increase concurrency, performance, and scalability. This flexibility enables those with the right amount of expertise to get every last ounce of throughput out of their applications. See [Configuring Transaction Isolation Levels](configuring-transaction-isolation-levels.md) for detailed information.

## Creating Private Components

In scenarios where you have several helper components in an application that are meant to be called only from other components within that application, this release of COM+ enables you to use a new property, IsPrivateComponent, to mark these components as private. (In the previous release of COM+, all components had to be public to have access to COM+ services, which means that these components could be activated from other applications.) A private component can be seen and activated only by other components in the same application, giving you more control over what functionality to expose. You need only document and maintain the public components, while making use of private components that cannot be accessed from outside the application but that can still take advantage of all COM+ services.

## DTC Security Settings

Several new security settings have been added for the Microsoft Distributed Transaction Coordinator (DTC), enabling you to customize your security levels for managing distributed transactions. See DTC Security Considerations about these settings and how to implement them.

To facilitate mutual authentication, the DTC is restricted to running under the NetworkService account. See Managing Accounts and Privileges for detailed information.

For recovery with XA databases, it is recommended that the NetworkService account be provided the permissions and roles needed to perform this recovery. The exact method of doing this is specific to each database. See Disabling Native Distributed Transactions and Disabling TIP and XA Transactions for more information.

To help provide a more secure system when using XA transactions, Windows Server 2003 platforms include a new registry entry for specifying XA DLL files. When upgrading to Windows Server 2003, you can work with XA transactions as before by creating a registry entry under **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\MSDTC\\XADLL**, where the value name is the name of the DLL (in the format *dllname*.dll) and the value is the full path of the DLL file. You need to create an entry for each XA DLL file in use. If the computer running DTC is part of a cluster, the registry entry needs to be made for each node in the cluster. See Managing XA Transactions for more information.

## Low-Memory Activation Gates

With this release, COM+ automatically checks memory before creating a COM+ server or object. If the percentage of virtual memory available to the application falls below a fixed threshold, the activation fails before the object is created. By failing these activations that would normally run, the [COM+ Low-Memory Activation Gates](com--low-memory-activation-gates.md) service greatly enhances system reliability.

## Moving and Copying COM Components

With this release, COM+ allows you to move and copy your components. This means you can configure a single physical implementation of a component many different times. You get component reuse at a binary level rather than at the source code level, which results in less code, lower development costs, and faster time to market. See [Moving Components](moving-components.md) and [Copying Components](copying-components.md) for detailed information.

## Network Access

COM+ network access is disabled by default on Windows Server 2003, meaning that COM+ can be used only locally by default. Use the following procedure to enable network COM+ access.

**To enable network COM+ access**

1.  On the **Start** menu, point to **Control Panel**, then select **Add or Remove Programs**.

2.  Click **Add/Remove Windows Components**.

3.  Select **Application Server** and click **Details**.

4.  Check the box next to **Enable network COM+ access**, and then click **OK**.

5.  Click **Next** to complete the Windows Components wizard.

6.  Click **Finish** to close the wizard.

DTC network transactions access is disabled by default on Windows Server 2003. On these platforms, the DTC can perform only local transactions by default. Use the following procedure to enable network DTC access.

> [!NOTE]
> You can also enable network DTC access by using the Component Services administrative tool or programmatically through the COM+ Administration Library. For procedural information, see "Configuring DTC Security" in the Component Services Administration Help.

**To enable network DTC access**

1.  On the **Start** menu, point to **Control Panel**, then select **Add or Remove Programs**.

2.  Click **Add/Remove Windows Components**.

3.  Select **Application Server** and click **Details**.

4.  Check the box next to **Enable network DTC access**, and then click **OK**.

5.  Click **Next** to complete the Windows Components wizard.

6.  Click **Finish** to close the wizard.

## Pausing and Disabling Applications

COM+ applications are now more manageable. An administrator can pause and resume COM+ server applications or disable and enable COM+ library or server applications, or even individual configured components. Both the pausing and disabling features prevent future activations without affecting existing component instances. See "Administering COM+ Applications" in the Component Services Administration Help for more information.

## Process Dumping

It's not easy troubleshooting applications in a production environment. How do you gather information on a problem without disturbing the running processes? COM+ now provides a solution through its new process dump feature. This feature allows the system administrator to dump the entire state of a process without terminating it. See "Administering the Process Dump Tool for Debugging COM+ Applications" in the Component Services Administration Help for more information.

## Process Initialization

Many server applications need to do specific initialization and cleanup when they are started and shut down. When running on Windows Server 2003, you can create a class that implements the [**IProcessInitializer**](/windows/desktop/api/ComSvcs/nn-comsvcs-iprocessinitializer) interface. When the process starts up, it calls [**IProcessInitializer::Startup**](/windows/desktop/api/ComSvcs/nf-comsvcs-iprocessinitializer-startup) and when shutting down, it calls [**IProcessInitializer::Shutdown**](/windows/desktop/api/ComSvcs/nf-comsvcs-iprocessinitializer-shutdown). This gives your component the opportunity to do needed tasks, such as initializing connections, files, and caches.

## Running COM+ Applications as NT Services

COM+ developers can now use the Component Services administrative tool to configure and implement a COM+ server application as an NT service. This means that the server can be automatically started or restarted if your application always needs to be running; that your COM+ application can run as the local system account if it needs to perform privileged operations; and that your application's dependent services can now be started automatically. See [COM+ Applications Running as Service Applications](com--applications-running-as-service-applications.md) for detailed information.

## Side-by-Side Assemblies

Side-by-side (SxS) assemblies allow applications to specify which version of a system DLL or classic COM component to use, such as MDAC, MFS, MSVCRT, or MSXML. For example, if an ASP application relies on MSXML version 2.0, you can ensure that this application still uses MSXML version 2.0 even after service packs are applied to the server. That is, even when a new version of MSXML is installed on the computer, version 2.0 remains and is used by your application.

To configure SxS assemblies, you need to know the path to the DLL and that the COM+ manifest file exists in every virtual directory that needs to use the DLL. The COM+ manifest is an XML file that has information about where a DLL is installed. The manifest is used to create an activation context for the application. Activation contexts allow an application to load a particular DLL version, COM object instance, or custom window version. You can use the Component Services administrative tool or ApplicationDirectory property to enter the full path of the application root directory that contains a valid SxS assembly manifest file. For more information, see [Isolated Applications and Side-by-side Assemblies](/windows/desktop/SbsCs/isolated-applications-and-side-by-side-assemblies-portal).

## Windows Error Reporting

COM+ 1.5 includes support for the Windows Error Reporting (WER) component, available starting in Windows XP. WER enables users to notify Microsoft of application faults, kernel faults, and unresponsive applications. These notifications allow the Microsoft customer support teams to solve technical problems more effectively. In addition, the Windows Error Reporting component enables COM+ developers to receive information that can be used to improve their applications. For more information, see [Windows Error Reporting](/windows/desktop/wer/windows-error-reporting).

 

 
