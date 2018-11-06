---
title: Publishing with Service Connection Points
description: The Active Directory Schema defines a serviceConnectionPoint (SCP) object class to make it easy for a service to publish service-specific data in the directory.
ms.assetid: 3544aa64-ecb0-48a1-ae49-05247a983842
ms.tgt_platform: multiple
keywords:
- Publishing with Service Connection Points AD
- service connection points AD
- service connection points AD , publishing with
ms.topic: article
ms.date: 05/31/2018
---

# Publishing with Service Connection Points

The Active Directory Schema defines a **serviceConnectionPoint** (SCP) object class to make it easy for a service to publish service-specific data in the directory. Clients of the service use the data in an SCP to locate, connect to, and authenticate an instance of your service.

This section provides an overview of service connection points and code examples that show how a client/service application uses SCPs.

The code example follows these steps to implement service publication with SCPs.

For more information and a code example that performs these steps, see [Creating a Service Connection Point](creating-a-service-connection-point.md).

**To create SCPs in the directory at service installation**

1.  Bind to the computer object for the host computer on which the service instance is installed.
2.  Create an SCP object as a child of the computer object, specifying the initial values for the attributes of the SCP.
3.  Set access control entries (ACEs) in the security descriptor of the SCP object to enable the service to modify SCP properties at run time.
4.  Cache the **objectGUID** of the SCP in the registry on the service's host computer.

For more information and a code example that performs these steps, see [Updating a Service Connection Point](updating-a-service-connection-point.md).

**To update the SCP attributes at service startup**

1.  Retrieve the **objectGUID** from the registry and use it to bind to the SCP.
2.  Retrieve attributes, such as **serviceDNSName** and **serviceBindingInformation**, from the SCP. Compare these values to the current values and update the SCP if necessary.

For more information and a code example that performs these steps, see [How Clients Find and Use a Service Connection Point](how-clients-find-and-use-a-service-connection-point.md).

**To find and use an SCP by a client application**

1.  Bind to the Global Catalog and search for objects with a **keywords** attribute that matches the service's product GUID. Each object found is an instance of the service. Select an instance and retrieve the distinguished name of the SCP.
2.  Use the distinguished name to bind to the SCP.
3.  Retrieve the values of various attributes from the SCP, such as **serviceDNSName** and **serviceBindingInformation**. Use these values to connect to and authenticate the service instance.

For more information about what roles can create and update an SCP, see [Security Issues for Service Publication](security-issues-for-service-publication.md).

For more information about where to create an SCP, see [Where to Create a Service Connection Point](where-to-create-a-service-connection-point.md).

For more information about the kind of data to store in an SCP, see [Service Connection Point Properties](service-connection-point-properties.md).

For more information about how a service installer and the service work together to maintain current data in an SCP, see [Creating and Maintaining a Service Connection Point](creating-and-maintaining-a-service-connection-point.md).

 

 




