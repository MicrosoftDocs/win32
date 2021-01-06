---
description: The Microsoft distributed programming model consists of several technologies, including MSMQ, IIS, DCOM, and COM+. All of these services were designed for use by distributed applications.
ms.assetid: c72bbd47-0219-40ba-a7d5-2a6b725972d0
title: COM+ Design Assumptions and Principles
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Design Assumptions and Principles

The Microsoft distributed programming model consists of several technologies, including MSMQ, IIS, DCOM, and COM+. All of these services were designed for use by distributed applications.

COM+ was developed to make creating distributed applications easier. The overall architecture is based on a set of assumptions and principles.

## Assumptions

The assumptions are as follows:

-   **The COM+ application will support multiple users across multiple servers.** In other words, you are building a distributed application, and these multiple users are going to be on different host computers from where the code runs. Users are going to access the code via the Internet or via a private network. The user interface is going to be presented via browser or perhaps a custom application, such as a form-based application written with Microsoft Visual Basic or MFC. That user interface is going to be located on the client computer.
-   **The COM+ application can be made scalable and can provide greater availability and reliability by deploying the application across multiple server computers.** By doing this, you can balance the workload of the application and provide fault tolerance by using Windows Clustering.
-   **If things go wrong, the state of the persisted data, stored in a database, from a COM+ application will be maintained if you are using transactions.** The application state must survive accidents that can occur, such as application errors, system crashes, or network failures.

## Principles

In addition to these three assumptions, the following principles pervade the COM+ programming model:

-   **The application logic will reside on server computers, not on client computers.** There are three major reasons to do this:
    -   The client computer may not have the processing power or features needed to run the application logic. In addition, keeping the application logic on the server simplifies deployment.
    -   The server computers are often closer to the data, and this data is most often in a database. Because your application is accessing databases, you want to be very sensitive to the cost of database connections. By putting most of the logic on the server computers, you can share database connections and get a significant performance improvement. There are other resources on the server computers that can be shared as well, again with a performance benefit.
    -   Having application logic reside on server computers keeps control of the security context with the application. You have more control over security if you maintain that security on application components running on server computers rather than on client computers.
-   **Transactions are the core.** By design, transactions so permeate the COM+ programming model that it is very important for you to understand them. While you can make use of many of the services of COM+ without using transactions, if you choose not to use them, you cannot take full advantage of the COM+ services available to you. Some important benefits of using transactions include the following:
    -   Transactions are a reasonable solution for the problem of concurrency management. Also, transactions help protect against crashes and have a good error recovery model. In addition, transactions turn out to be a great way to manage tasks across multiple systems.
    -   You can design a transaction-based COM+ application to work with a resource manager and a database, which helps protect most state information. By keeping state inside a database or some other storage managed by a resource manager, you don't have to keep much state inside the actual objects your application creates. While this is a departure from a pure object-oriented model, it works well for creating distributed applications with error recovery.
-   **Application functionality is built as COM objects, wrapping the protocols used to communicate with other systems or technologies.** Because you are probably building components that are going to stitch together several technologies or legacy systems, plan on using a variety of communication protocols. Use HTTP for client/server communication or application-to-application communication over the Internet. Use DCOM for application-to-application or component-to-component communication on the server.

## Related topics

<dl> <dt>

[Basic Guidelines for Designing COM+ Applications](basic-guidelines-for-designing-com--applications.md)
</dt> <dt>

[Designing the COM+ Application Using UML](designing-the-com--application-using-uml.md)
</dt> <dt>

[General Design Tips for Using COM+](general-design-tips-for-using-com-.md)
</dt> <dt>

[Optimizing Interactions with the COM+ Business Logic Tier](optimizing-interactions-with-the-com--business-logic-tier.md)
</dt> <dt>

[Other Microsoft Tools for Building Distributed Applications](other-microsoft-tools-for-building-distributed-applications.md)
</dt> </dl>

 

 



