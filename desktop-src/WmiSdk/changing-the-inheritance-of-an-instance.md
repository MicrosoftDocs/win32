---
description: You may find a situation where an instance that was created as a child of one parent class must change parent classes and become the child of a different parent class.
ms.assetid: 6d0fd456-81ab-4665-bb88-f9fb29fbbd39
ms.tgt_platform: multiple
title: Changing the Inheritance of an Instance
ms.topic: article
ms.date: 05/31/2018
---

# Changing the Inheritance of an Instance

You may find a situation where an instance that was created as a child of one parent class must change parent classes and become the child of a different parent class. For example, you may have a derived class, **ManualService**, describing a manual service, and a derived class, **AutoService**, describing an automatic service. Both classes have a large number of properties. Not all properties are identical. To change a service from manual to automatic, you must also change the instance representing the service from **ManualService** to **AutoService**. In the current version of WMI, you cannot call the [**IWbemServices::PutInstance**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstance) method with the *pInst* parameter pointing to an instance of **AutoService** and the key properties describing the **ManualService** instance. If you do, you implicitly delete the original **ManualService** instance. In essence, after you establish the class of an instance, you can only change the parent class of an instance by deleting the instance and recreating the instance as an instance of the new parent class.

The following procedure describes how to move an instance from one class to another class.

**To move an instance from one class to another class**

1.  Delete the instance from the original class.
2.  Create the instance under the new class.

    WMI does not allow applications to move an instance by creating it in the new class and then updating it with the key of the original instance.

For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md).

 

 



