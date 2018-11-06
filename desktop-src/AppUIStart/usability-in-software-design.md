---
title: Usability in Software Design
description: This topic introduces the concept of usability and why it should be an important part of any software design project.
ms.assetid: 912b3224-e36d-44d6-98fa-a7f28e68a2d0
ms.topic: article
ms.date: 05/31/2018
---

# Usability in Software Design

This topic introduces the concept of usability and why it should be an important part of any software design project.

-   [Introduction](#introduction)
-   [Defining Usability](#defining-usability)
    -   [Ease of Use](#ease-of-use)
    -   [Usability vs. Utility](#usability-vs-utility)
    -   [Liking It vs. Using It](#liking-it-vs-using-it)
    -   [Discovery vs. Learning vs. Efficiency](#discovery-vs-learning-vs-efficiency)
    -   [Slogans Do Not Work](#slogans-do-not-work)
-   [Why is Usability Important?](#why-is-usability-important)
    -   [Why Should You Care?](#why-should-you-care)
    -   [What Does It Cost?](#what-does-it-cost)
    -   [How Do I Increase Usability?](#how-do-i-increase-usability)
    -   [Why Should I Involve Users?](#why-should-i-involve-users)
    -   [Can't I Just Follow Guidelines?](#cant-i-just-follow-guidelines)
    -   [Do I Need to Build a Usability Lab?](#do-i-need-to-build-a-usability-lab)
    -   [How Do I Get Started?](#how-do-i-get-started)

## Introduction

The term "usability" in the context of creating software represents an approach that puts the user, instead of the system, at the center of the process. This philosophy, known as user-centered design, incorporates user concerns and advocacy from the beginning of the design process and dictates that the needs of the user should be that most important of any design decisions.

The most visible aspect of this approach is usability testing, in which users work and interact with the product interface and share their views and concerns with the designers and developers.

## Defining Usability

The section defines what usability means in the context of software development and how it relates to other aspects of the development process.

### Ease of Use

Usability is a measure of how easy it is to use a product to perform prescribed tasks. This is distinct from the related concepts of utility and likeability.

### Usability vs. Utility

A central attribute that determines a product's quality is usefulness. This measures whether the actual uses of a product can achieve the goals that the designers intend for them to achieve. The concept of usefulness branches further into utility and usability. Although these terms are related, they are not interchangeable.

Utility refers to the ability of the product to perform a task or tasks. The more tasks the product is designed to perform, the more utility it has.

Consider typical Microsoft MS-DOS word processors from the late 1980s. Such programs provided many powerful text editing and manipulation features, but required users to learn and remember dozens of arcane keystrokes to perform them. Applications such as these can be said to have high utility (they give users the necessary functionality) but low usability (the users must spend lots of time and effort to learn and use them). By contrast, a well-designed, simple application such as a calculator may be very easy to use but not offer much utility.

Both qualities are necessary for market acceptance, and both are part of the overall concept of usefulness. Obviously, if a program is highly usable but does not do anything of value, nobody will use it. And users who are presented with a powerful program that is difficult to use will likely resist it or seek out alternatives.

Usability testing helps you determine how easy it is for users to perform particular tasks. However, it does not directly help you determine if the product itself has value or utility. (Users may volunteer utility-related comments during usability testing, but any comments should be verified with other, more robust research methods.)

### Liking It vs. Using It

Likeability is always a desirable trait in a product. If people like the product, they are more likely to use it and to recommend it to other people. But as with utility, you should be careful not to confuse likeability with usability.

People frequently like a product for reasons unrelated to utility and usability. They may be attracted to its style, or to the status they believe that the product confers upon them. People typically like highly usable products, but you should not assume that means a well-liked product is usable.

Usability is about whether a person can use the product to perform the tasks that they need to perform. Usability testing primarily measures performance, not preference. However, standardized questionnaires can be used to measure preferences across products.

### Discovery vs. Learning vs. Efficiency

There are many aspects to usability, but traditionally the term refers specifically to the attributes of discovery, learning, and efficiency.

-   Discovery involves looking for, and finding, a product's feature in response to a particular need. Usability testing can determine how long it takes a user to find a feature and how many errors (wrong choices about location) the user makes along the way.
-   Learning refers to the process by which the user understands how to use a discovered feature to complete a task. Usability testing can determine how long this process takes and also how many errors the user makes while learning the feature.
-   Efficiency refers to the point at which the user has "mastered" the feature and uses it without requiring further learning. Usability testing can determine how long it takes for the experienced user to execute the steps necessary to use the feature.

These three basic aspects of usability are strongly influenced by the nature of the task at hand and the frequency with which the user performs it. Some features are used so seldom or are so complex that the user essentially relearns them every time; for these features, Microsoft often develops wizards to guide the user through the process.

### Slogans Do Not Work

Software developers sometimes think that simple slogans like "make the product more usable" will help solve usability problems. While a positive attitude toward usability is important, only proper usability testing with ordinary users, in the context of the specific product being created, can provide developers with the information they need to create a product that will fulfill the users' needs. "Make the product more usable" should be the slogan of every software developer, but it only makes sense if the developer knows what usability means. Testing with ordinary users is the most reliable way to find out.

## Why is Usability Important?

The section answers some common questions about why usability is important and how to incorporate user-centered design principles into the development process.

### Why Should You Care?

If usability considerations haven't already been incorporated into the product design process, you might wonder why it is necessary or desirable. After all, it's certainly possible to release a working, bug-free product without performing any usability work at all. But incorporating user-centered design principles can lead to a much-improved product in several areas.

The best reason to perform usability testing is to reduce the number of support calls from users. Poor usability is a major reason why users call software technical support lines, and every software company executive and Information Services manager knows how expensive product support can be. Plus, charging users for support increases potential dissatisfaction with the product. If users find it easy to use your product, they will not need to call for technical support as often.

For software produced for internal use, the next best reason to make usability an important part of the development process is to reduce training costs. A highly usable product is much easier for users to learn than one for which usability was not a high priority. Users learn features more quickly and retain their knowledge longer, which directly correlates to decreased training costs and time.

Usability testing helps improve user acceptance. Acceptance results from a number of factors, including usability, utility, and likeability. For retail products, user acceptance often directly correlates to repeat buying or to loyalty, which means the user is likely to recommend the product to others. For internal applications, user acceptance correlates to a willingness to use the software to perform the tasks for which it was designed, which helps increase productivity. Increasing usability is one of the factors that can contribute to increased user acceptance.

Usability can help differentiate your products from those of your competitors. If two products are substantially equal in utility, the product with better usability will probably be regarded as superior. In addition, the Windows look-and-feel and accompanying programming guidelines have leveled the playing field for the basic user interface, so that many programs that serve similar functions look and act somewhat alike. These similarities mean that small differences in usability can have a big effect on user preference.

Finally, every product gets tested for usability eventually. Users perform usability testing on the product every time they use it, and they render their verdict through their continued use or lack thereof. Testing the product before releasing it to market can help ensure that users' experiences with the product are positive.

### What Does It Cost?

Software developers and project managers often worry that initiating a user-centered design process and performing proper usability testing will require unacceptable amounts of time and money. The reality is that the cost in time and money spent focusing on the user is often relatively small, and certainly so when compared to the cost of not doing it.

Consider, for example, the cost in time and money of making design revisions late in the development cycle as opposed to earlier, when the product is still on the drawing board. Waiting until the beta period to expose users to the product for purposes of usability testing may result in the dismantling of parts of the program that took a lot of time to develop. And waiting until the product is actually released and then making changes based on negative feedback or supporting a poor design could make the cost immeasurably higher due to high product-support costs or poor reception by users.

A reasonable usability study can typically be performed in about two weeks or less, and can greatly reduce the time and cost of making changes late in the development cycle. The cost of performing testing will vary depending on the nature of the product and the parts of the interface that are tested.

Think of usability testing as being akin to code testing. Successful project managers account for code testing when planning a development project. They do not see it as something extra that must be tacked on to the project schedule and budget. Rather, project managers accept code testing as a cost of doing business because the alternative is so much more expensive. The same applies to usability testing.

### How Do I Increase Usability?

Upon reading and understanding the importance of usability, software developers are sometimes tempted to add usability, as if it were an ingredient that can simply be added to a product to make it more usable. Instead, usability should be part of the design process itself, rather than a "thing" that is added to the process here or there. The reason that usability experts refer to "user focus" and "user-centered design" is that usability depends on keeping the needs of users central to the design process. User-centered design by necessity involves more than just following a set of rules governing button and menu placement in an interface. Usability testing is an opportunity to check the design work. It is not a way to "add" usability to a product.

Gould, Boies, and Lewis (1991) identify four important tenets of user-centered design:

-   Early focus on users.

    Developers should concentrate on understanding the needs of the users early in the design process.

-   Integrated design.

    All aspects of the design should evolve in parallel, rather than in sequence. Keep the internal design of the product consistent with the needs of the user interface.

-   Early and continual testing.

    The only currently feasible approach to software design is an empirical one: the design works if real users decide it works. Incorporating usability testing throughout the development process gives users a chance to deliver feedback on the design before the product is released.

-   Iterative design.

    Big problems often mask small problems. Designers and developers should revise the design iteratively through rounds of testing.

### Why Should I Involve Users?

Developers should recognize that they are not typical users. They have more intimate knowledge and understanding of the system that they are developing than the average user ever will. Aspects of the interface that are unclear or confusing to most users might therefore be perfectly clear to someone who has worked on the project. Some software developers are able to empathize with the average user to a degree, but there is no substitute for the real interactions of actual users with the product.

Accordingly, by focusing on typical users' needs early and revising the design based on user testing often, user-focused software developers produce better designs and, as a result, better products.

With a better design comes better acceptance from users. The benefit with retail software is obvious: increased sales. Acceptance is also important with software developed for internal use: increased focus on user-centered design leads to increased productivity and a diminished need for support. Visibly involving users from the beginning of development also demonstrates an interest in their concerns and needs, which increases their willingness to help in the development effort.

### Can't I Just Follow Guidelines?

Microsoft has developed a set of interface guidelines for the Windows computing platform to ensure that Windows programs have a consistent look and feel. Other companies have developed similar guidelines for other computing platforms, and usability experts like Jakob Nielsen have written extensively on designing usable Web pages. With the wealth of information available on these topics, designers sometimes believe rigorous adherence to guidelines and standards is all that is necessary to produce usable products.

The problem with this approach is that guidelines are inherently general. Guidelines must apply to a wide variety of cases and therefore do not always prescribe the best course of action for the particular application being developed. Adhering to a well-written set of guidelines may help in the design of a consistent interface, but they cannot guarantee it's usablility unless it's tested with real users. When using guidelines, do not use them like a cookbook where guidelines point the way toward the best of all outcomes. Two developers can implement the same guideline in two different ways, and both implementations might not be equally appropriate for the situation. Occasionally, rigorous adherence to guidelines can lead to poor results or to conflicts between guidelines. Only user-centered design can help flush these issues out before they become problems.

Another way of thinking about this is: Let user-centered design be the arbiter of design decisions, not user interface guidelines.

### Do I Need to Build a Usability Lab?

Do not assume that usability testing means committing to an expensive lab, with ceiling-mounted cameras, one-way mirrors, and other focus-group trappings. To be sure, companies that do a lot of testing often find it convenient to build dedicated labs, and usability consultants often have a wide range of facilities and equipment to offer their clients. But useful, valid usability testing can be performed in a variety of settings and circumstances.

One approach is to simply have a tester?someone versed in performing human participant studies and collecting data?sit behind a user as he or she works and observe the user performing tasks. This can easily be performed in a conference room or an office. For more information on testing by observation, see the Dumas and Redish entry in [Other Resources](other-resources.md).

As usability testing develops and becomes more involved, equipment such as a video camera, a one-way mirror, or tools that allow you to view and record a user's monitor in real time can be added.

Alternatively, testing can be outsourced to usability consultants. The following section contains tips on finding the right consultants.

### How Do I Get Started?

Once it has been decided to incorporate user-centered design principles into the development process, you will need to decide whether to hire usability professionals or outsource the usability testing to a vendor.

The Usability Professionals Association (UPA) has a vendor guide that can help find usability consultants.

Some consulting groups can also help set up usability labs or develop an in-house usability program to incorporate usability principles into the design process.

If hiring usability professionals, the Human Factors and Ergonomics Society has a placement service that can help find potential employees. Many usability professionals also belong to ACM Special Interest Group on Computer-Human Interaction (SIGCHI) and UPA. Place employment ads in their publications or at their conferences.

Whichever route is taken, remember that these are testing services. The principle that designers are not typical users is also true of usability professionals.

For more information on these companies and organizations and to find out more about usability testing and user-centered design, see [Other Resources](other-resources.md).

 

 




