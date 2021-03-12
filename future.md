### How can we move it to internet?

Frontend

    1. Go for hybrid app development like react-native, flutter
        1. One codebase and develop for multiple platform
        2. Fast development with once pass the learning curve line
    2. Native platform development, 
        1. will give you fast development with minimal learning 
        2. Multiple codebase and team dependencies/involvement
    3. There are several pros and cons associated with native vs hybrid
    4. IMO, It is better to start with hybrid one for phase 1, where more focus is on deliverable. Move fast and break things.

Backend

    1. For phase 1, we're not much worried about traffic, as mentioned it is about delivering the product. So marketing team can do their job.
    2. We can use cloud services & fasten up development with serverless approach
        1. API Gateway for micro services
        2. Socket with multiplayer support, chat https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html
        3. DynamoDB or RDS for persistent data store
    3. Again, there set up of challenges with serverless architecture like cost related (lambda warm up & boot time)
    4. It better to setup alerts on the billing metrics, act accordingly by choosing right stack after seeing actie user growth


### How can we design scalable system?

    Desktop Workflow

        1. User will land on website
        2. Participate in any available game or create a new game & share the links with friends
        3. User will join the game by invitation
        4. The game creator/ host will setup the setting for game & start it
        5. Based on the order, every player get their chance to roll the dice
        6. After every round completion, scoreboard wil be displayed
        7. Based on the given rules, needful validation will done

    Based on given workflow

        1. we can take advantage of serverless lambda to build required micro services
        2. Socket programming to exchange information real time to make more enjoyable
        3. Socket API is holds the all rules & business logic of the game
        4. Based on the traffic acquisition strategy, you can make decision to upgrading underline tech stack
        5. Moving ECS or fargate is strategic move & depends on many factors
        6. It is better to plan phase wise approach, design the phase of product release based on desired outcome expected by stakeholders

### How can we monetize the game?

Straight forward answer is ads.

Apart from that, there are many ways where you can monetize your app without ads.

`No ads = happy & returning customers`

Now, it's interactive game where multiple players can join, chat & play the game
    
    Here are the list of accessories which user can happily buy
        1. No ads with Shiny single/multi colour dice
        2. Multiple theme or background for rolling dice
        3. Special effects for dice
        4. virtual currency to participate in league matches

