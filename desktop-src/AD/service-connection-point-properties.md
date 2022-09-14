---
title: Service Connection Point Properties
description: The attributes of the serviceConnectionPoint class are sufficient for most services.
ms.assetid: 08888d2c-b46e-4b86-87e4-0c061ea147a0
ms.tgt_platform: multiple
keywords:
- Service Connection Point Properties
- service connection points AD , properties
ms.topic: article
ms.date: 05/31/2018
---

# Service Connection Point Properties

The attributes of the **serviceConnectionPoint** class are sufficient for most services. Active Directory Domain Services do not define how the attributes are used, so the clients of your service must be able to interpret and use the data in your service SCPs. Services that must publish additional data about themselves can extend the Active Directory schema by creating a subclass of the **serviceConnectionPoint** class, giving the subclass a distinct name. For more information about schema extensions, see [Extending the Schema](extending-the-schema.md).

The most important attributes of an SCP are **keywords**, **serviceDNSName**, **serviceDNSNameType**, **serviceClassName**, and **serviceBindingInformation**. Client applications search the directory for **keywords** values to locate your SCP. When your SCP is found, clients can read other attributes to retrieve service data.




| Attribute | Description | 
|-----------|-------------|
| <strong>keywords</strong><br /> | The <strong>keywords</strong> attribute can contain multiple string values that identify your service. This attribute is included in the Global Catalog, which means that clients in any domain of an enterprise forest can search the Global Catalog for keywords associated with your service. This attribute is also indexed, which improves query performance. The installer that creates the SCP sets the values of the <strong>keywords</strong> attribute. Typically, these values are not modified by the active service.<br /> The exact keywords you should include in your SCP depend on how clients search for your service. The best keywords to use are GUID strings because GUIDs are guaranteed to be unique in a forest. Use the GUID string format returned by the <a href="/windows/desktop/api/rpcdce/nf-rpcdce-uuidtostring"><strong>UuidToString</strong></a> function in the RPC library. You can also include human-readable names, if clients may use them to search for your service. The keywords in an SCP should include GUID strings and/or names that identify the following data about your service:<ul><li>Your company or organization: for example, Fabrikam.</li><li>The product or service: for example, SQL Server. This enables client applications to find SCPs for services of that type.</li><li>The specific version of the product or service, such as 7.5.</li><li>For SCPs that publish a specific set of data or capabilities for a type of service, include a GUID string or name that identifies the specific instance. For example, a database service could publish an SCP for a specific database. In this case, the SCP would include a product GUID to identify the service and another GUID to identify the database.</li></ul><br /> | 
| <strong>serviceDNSName</strong> and <strong>serviceDNSNameType</strong><br /> | Client applications use the <strong>serviceDNSName</strong> and <strong>serviceDNSNameType</strong> attributes to determine the service's host computer. The <strong>serviceDNSNameType</strong> value indicates the type of DNS name specified by <strong>serviceDNSName</strong> usually "A" if <strong>serviceDNSName</strong> contains a host name or "SRV" if <strong>serviceDNSName</strong> contains a SRV record name.<br /> The <strong>serviceDNSName</strong> value is typically the DNS name of the service's host computer. Your service installer can call the <a href="/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getcomputernameexa"><strong>GetComputerNameEx</strong></a> function to get the DNS name of the local computer.<br /> For services that have DNS SRV records, <strong>serviceDNSName</strong> can be the name of the SRV record. A client application uses the DNS APIs to retrieve all the SRV records that match this name. The client then retrieves the DNS host name from one of the SRV records. This technique is useful for replicated services because SRV records also include data that enables the client to select the best replica.<br /> | 
| <strong>serviceBindingInformation</strong><br /> | A multi-value property that contains string values that store data required to bind to a service. This property is indexed and is replicated to the Global Catalog.<br /> The content of <strong>serviceBindingInformation</strong> is specific to the service that published the SCP; clients must interpret the binding data. In the most common case, the binding data consists of a port number on the service host computer.<br /> | 
| <strong>serviceClassName</strong><br /> | A single-value property that identifies the class of service represented by the SCP. This is a descriptive string specific to the service that published the SCP; for example, SqlServer. For services that support mutual authentication, clients can use this property, along with the DNS name of the service's host computer, to form a service principal name. For more information, see <a href="mutual-authentication-using-kerberos.md">Mutual Authentication Using Kerberos</a>.<br /> | 




 

 

