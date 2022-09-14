---
description: Accessing the COM+ Catalog
ms.assetid: 1322a3fe-faee-4971-949f-5e0d2dfe469b
title: Accessing the COM+ Catalog
ms.topic: article
ms.date: 05/31/2018
---

# Accessing the COM+ Catalog

The COM+ catalog is the underlying data store that holds all COM+ configuration data. Whenever you do any kind of COM+ administration, you are reading and writing data stored in the catalog. The only way that you can access the catalog is through the Component Services administrative tool or through the COMAdmin library.

The COM+ catalog provides a layer of abstraction over the actual details of where and how COM+ configuration data is stored. Much of the data is stored in the COM+ registration database (or RegDB), which holds data for all configured components installed in COM+ applications. This database is used at application run time to provide configuration data to COM+ to properly activate objects in an appropriate context, enabling services to be provided for objects per their configuration. The RegDB itself is a transacted resource manager that uses DTC transactions through the [compensating resource manager](com--compensating-resource-manager.md); when you make persisted configuration changes, they are committed transactionally. The only way that you can access the RegDB is through the COM+ catalog, using the COMAdmin objects or the Component Services administrative tool.

On each computer, there is a COM+ catalog server running as a component in the system application. The catalog server controls access to the catalog data stored on its machine; in effect, the catalog server is a query engine that allows you to read and write data in the catalog on that machine. When you initiate programmatic administration by instantiating a [**COMAdminCatalog**](comadmincatalog.md) object, this object opens a session with the local catalog server. Requests for collections or collection items on the local catalog are handled by the local catalog server. When you connect to a remote machine, you are communicating with the catalog server on that machine.

## Security Considerations in Administration

To change data on the COM+ catalog, you need to have authority as an administrator. To use the Component Services administrative tool to change any configuration data, you need to be a member of the Administrators role assigned to the system application on the machine you are trying to administer. Likewise, to change any data by using the COMAdmin objects, your code needs to be running with Administrator authority. That is, an application or script using the COMAdmin objects must be running under a user account that is assigned to the Administrators role on the system application on the machine that it is trying to administer. The application can access and change information on the catalog only to the extent that the account under which it is running has that authority.

## Related topics

<dl> <dt>

[Overview of the COMAdmin Objects](overview-of-the-comadmin-objects.md)
</dt> <dt>

[Summary Description of the COMAdmin Classes](summary-description-of-the-comadmin-classes.md)
</dt> </dl>

 

 



