---
title: Creating a WHERE clause for the registry provider
description: The main points to consider when creating a proper WHERE clause for the System Registry provider is that each event query must be complete and explicit. Failure to be complete and explicit will result in an error message.
ms.assetid: cdef2900-8d1a-4f0b-8318-7463d90e4152
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Creating a WHERE clause for the registry provider

The main points to consider when creating a proper WHERE clause for the System Registry provider is that each event query must be complete and explicit. Failure to be complete and explicit will result in an error message.

To be complete, each event query in the *bstrQuery* parameter of [**ExecNotificationQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationqueryasync) must contain a WHERE clause that includes each of the properties in the specified event class.

The following example shows how to set *bstrQuery* to register for tree change events in the "HKEY\_LOCAL\_MACHINE\\Software" tree.


```sql
SELECT * FROM RegistryTreeChangeEvent  WHERE Hive = "HKEY_LOCAL_MACHINE" AND Rootpath = "Software"
```



To be explicit, the provider should be able to infer from the query a list of possible values for every property in the event class.

The following example shows the event query that correctly registers for tree change events.


```sql
SELECT * FROM RegistryTreeChangeEvent 
    WHERE (hive = "hkey_local_machine" AND rootpath = "software") 
    OR    (hive = "hkey_current_user" AND rootpath = "console")
```



The following is an example of an incorrect registration.


```sql
SELECT * FROM RegistryTreeChangeEvent  WHERE hive = "hkey_local_machine" OR rootpath ="software"
```



Because there is no way to evaluate the possible values for each of the properties, WMI rejects with the error WBEM\_E\_TOO\_BROAD any query that either does not have a WHERE clause or if the WHERE clause is too broad to be of any use.

 

 



