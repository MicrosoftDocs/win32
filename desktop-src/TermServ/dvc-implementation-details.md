---
title: DVC Implementation Details
description: This section contains information about how to write a dynamic virtual channel (DVC) client module.
ms.assetid: 338556d9-e9a7-4926-a09c-8e2ce1627467
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# DVC Implementation Details

This section contains information about how to write a dynamic virtual channel (DVC) client module.

## In this section

<dl> <dt>

[Writing a Client DVC Module](writing-a-client-dvc-component.md)
</dt> <dd>

To write a dynamic virtual channel (DVC) client module, you must first implement and register a Remote Desktop Connection (RDC) client plug-in.

</dd> <dt>

[DVC plug-in registration](dvc-plug-in-registration.md)
</dt> <dd>

Describes syntax for the dynamic virtual channel (DVC) plug-in entry for the Remote Desktop Connection (RDC) client.

</dd> <dt>

[Starting a DVC Listener](starting-a-dvc-listener.md)
</dt> <dd>

To establish a successful connection between two dynamic virtual channel (DVC) modules that are running on the Remote Desktop Connection (RDC) client and server, a DVC listener must be running and in a listening state.

</dd> <dt>

[Accepting a Connection](accepting-a-connection.md)
</dt> <dd>

At some point in time, the dynamic virtual channel (DVC) client will request a connection to the DVC listener.

</dd> <dt>

[Writing Data by Using a DVC Channel](writing-data-by-using-a-dvc-channel.md)
</dt> <dd>

Writing channel data by using a dynamic virtual channel (DVC) is symmetric for both the Remote Desktop Session Host (RD Session Host) server and the client.

</dd> <dt>

[Testing and Debugging](testing-and-debugging.md)
</dt> <dd>

There is an "echo" listener that is implemented by the Remote Desktop Connection (RDC) client, which is always present and listening for incoming connections.

</dd> <dt>

[DVC Client Plug-in Example](dvc-client-plug-in-example.md)
</dt> <dd>

C++ code sample that shows how to create a Remote Desktop Connection (RDC) client dynamic virtual channel (DVC) plug-in.

</dd> <dt>

[DVC Server Module Example](dvc-server-component-example.md)
</dt> <dd>

C++ code sample that shows how to create the server-side dynamic virtual channel (DVC) module.

</dd> </dl>

 

 




