# Hands-On Docker for Microservices with Python 

<a href="https://www.packtpub.com/web-development/hands-on-docker-for-microservices-with-python?utm_source=github&utm_medium=repository&utm_campaign=9781838823818"><img src="https://www.packtpub.com/media/catalog/product/cache/e4d64343b1bc593f1c5348fe05efa4a6/9/7/9781838823818-original.png" alt="Hands-On Docker for Microservices with Python " height="256px" align="right"></a>

This is the code repository for [Hands-On Docker for Microservices with Python ](https://www.packtpub.com/web-development/hands-on-docker-for-microservices-with-python?utm_source=github&utm_medium=repository&utm_campaign=9781838823818), published by Packt.

**Design, deploy, and operate a complex system with multiple microservices using Docker and Kubernetes**

## What is this book about?
Microservices architecture helps create complex systems with multiple, interconnected services that can be maintained by independent teams working in parallel. This book guides you on how to develop these complex systems with the help of containers.

This book covers the following exciting features:
* Discover how to design, test, and operate scalable microservices 
* Coordinate and deploy different services using Kubernetes 
* Use Docker to construct scalable and manageable applications with microservices 
* Understand how to monitor a complete system to ensure early detection of problems 
* Become well versed with migrating from an existing monolithic system to a microservice one 
Use load balancing to ensure seamless operation between the old monolith and the new service

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/B081CSGDCS) today!

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
class ThoughtModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    text = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, server_default=func.now())
```

**Following is what you need for this book:**
This book is aimed at developers or software architects who work with complex systems and want to be able to scale the development of their systems.

It is also aimed at developers who typically deal with a monolith that has grown to a point where adding new features is difficult and development is difficult to scale. The book outlines the migration of a traditional monolithic system to a microservice architecture, providing a roadmap covering all the different stages.

With the following software and hardware list you can run all code files present in the book (Chapter 1-).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-10 | Python 3.8 | Windows/Linux/macOS |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781838823818_ColorImages.pdf).

## Errata
* Page 7 (Paragraph 2, Line 1): **Chapter 1, Making the Move – Design, Plan, Execute, describes a typical situation for a monolith system…** _should be_ **Chapter 1, Making the Move – Design, Plan, and Execute, describes a typical situation for a monolith system…** 
* Page 10 (Paragraph 4, Line 1): **a frontend web server that exposes the port in HTTP/HTTPS, and a backend that runs the monolith code in a dedicated web worker.** _should be_ **a frontend web server that exposes the port in HTTP/HTTPS and a backend one that runs the monolith code in a dedicated web worker.**
* Page 11 (Paragraph 2, Line 1): **Each individual deployed web worker will...** _should be_ **Each individually deployed web worker will...**
* Page 11 (Paragraph 6, Line 1): **As the service is a whole, any...** _should be_ **For the service is a whole, any...**
* Page 13 (Paragraph 6, Line 2): **...problem, but limiting its use so that it is contained, not requiring a drastic change in the company.** _should be_ **...problem. However, this technique's use should be restricted so that it is contained and does not require a drastic change in the company.**
* Page 40 (Paragraph 2, Line 2): **API interface** _should be_ **API**
* Page 41 (Paragraph 3, Line 2): **We will discuss different elements such as the API design, the database schema that supports it, and how to implement and how to implement the microservice.** _should be_ **We will discuss different elements such as the API design, the database schema that supports it, and how to implement the microservice.**
* Page 42 (Paragraph 1, Line 3): **Installation and running instructions can be found on its README.md file.** _should be_ **Installation and running instructions can be found in the README.md file.**
* Page 42 (Paragraph 3, Line 1): **The diagram shows the different elements for our example system…** _should be_ **The diagram shows the different elements in our example system…**
* Page 42 (Paragraph 4, Line 1): **Thoughts Backend will be responsible for storing new thoughts…** _should be_ **Thoughts Backend is responsible for storing new thoughts…**
* Page 43 (Paragraph 1, Line 4): **logged user** _should be_ **logged in user**
* Page 43 (Paragraph 2, Line 1): **Note the fact that the user is logged also validates the fact that the user exists.** _should be_ **The fact that the user is logged in also validates their existence.**
* Page 43 (Paragraph 4, Line 2): **The JWT itself is encrypted, but the information contained here is mostly only relevant for checking the user that was logged.** _should be_ **The JWT itself is encrypted, but the information contained here is mostly only relevant for checking the user who was logged in.**
* Page 43 (Last paragraph, Line 2): **API interface** _should be_ **API**
* Page 44 (Paragraph 3, Line 3): **at the client** _should be_ **at the client side**
* Page 45 (Paragraph 1, Line 1): **API interface** _should be_ **API**
* Page 45 (Line 7): **Any user, even not authenticated, can perform these actions.** _should be_ **Any user, even non-authenticated ones, can perform these actions.**
* Page 47 (Paragraph 1, Line 2): **There are two approaches to dealing with databases…** _should be_ **There are two approaches to deal with databases…**
* Page 47 (Last paragraph, Line 7): **A well-tailored SQLAlchemy definition can perform some abstract tasks very efficiently, but it requires good knowledge of the tool.** _should be_ **A well-tailored SQLAlchemy definition can perform some abstract tasks very efficiently, but you need to possess good knowledge of the tool.**
* Page 67 (Paragraph 1, Line 1): **API interface** _should be_ **API**
* Page 274 (Paragraph 4, Line 1): **logged user** _should be_ **logged in user**

### Related products
* Hands-On Microservices with Kubernetes  [[Packt]](https://www.packtpub.com/virtualization-and-cloud/hands-microservices-kubernetes?utm_source=github&utm_medium=repository&utm_campaign=9781789805468) [[Amazon]](https://www.amazon.com/dp/1789805465)

* Expert Python Programming - Third Edition  [[Packt]](https://www.packtpub.com/application-development/expert-python-programming-third-edition?utm_source=github&utm_medium=repository&utm_campaign=9781789808896) [[Amazon]](https://www.amazon.com/dp/1789808898)

## Get to Know the Author
**Jaime Buelta**
has been a professional programmer since 2002 and a full-time Python developer since 2010. He has developed software for a variety of fields, focusing, in the last 10 years, on developing web services in Python in the gaming and finance industries. He has seen first hand the revolution of containerization for backend services over the years and has seen how they can improve the development process. He published his first book, Python Automation Cookbook, in 2018. He is a strong proponent of automating everything to make computers do most of the heavy lifting so that users can focus on the important stuff. He is currently living in Dublin, Ireland, and is a regular speaker at PyCon Ireland.

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.
