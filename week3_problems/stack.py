# use list as a stack

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

# press back button
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])

if not browsing_session:
    browsing_session[-1]
