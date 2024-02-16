import time

# Function for user authentication
def authenticate_user(username, password):
    # Implement your authentication logic here
    # For simplicity, we'll assume any non-empty username and password are valid
    return bool(username) and bool(password)

# Function for session control
def manage_session_duration(session_start_time, max_session_duration):
    current_time = time.time()
    session_duration = current_time - session_start_time
    return session_duration <= max_session_duration

# Function for idle period tracking
def track_idle_period(last_activity_time, max_idle_duration):
    current_time = time.time()
    idle_duration = current_time - last_activity_time
    return idle_duration <= max_idle_duration

# Main function
def main():
    # Example usage of functions
    username = input("Enter username: ")
    password = input("Enter password: ")

    if authenticate_user(username, password):
        print("Authentication successful!")

        max_session_duration = 3600  # 1 hour
        max_idle_duration = 300  # 5 minutes

        session_start_time = time.time()
        last_activity_time = session_start_time

        while manage_session_duration(session_start_time, max_session_duration):
            if track_idle_period(last_activity_time, max_idle_duration):
                # Simulate network activity
                print("User is active. Network activity ongoing...")
                last_activity_time = time.time()
            else:
                print("User has been idle for too long. Disconnecting...")
                break

        print("Session ended.")
    else:
        print("Authentication failed.")

def test_authenticate_user():
    assert authenticate_user("user1", "password123")
    assert not authenticate_user("", "password123")
    assert not authenticate_user("user1", "")

def test_manage_session_duration():
    assert manage_session_duration(time.time(), 3600)
    assert not manage_session_duration(time.time() - 7200, 3600)

def test_track_idle_period():
    assert track_idle_period(time.time(), 300)
    assert not track_idle_period(time.time() - 600, 300)

if __name__ == "__main__":
    main()
