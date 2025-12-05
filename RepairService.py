def repair_service_trace():
    n = int(input( "Enter number of customers: ") )

    customers = []
    for _ in range(n):
        A, L, S, R = map(int, input("Enter A, L, S, R for customer: ").split())
        customers.append([A, L, S, R])

    order = list(map(int, input("Enter the order of customers to be served (space-separated indices): ").split()))

    time = 0
    location = 0
    service_order = []

    print("=== TRACE START ===")

    for customer_id in order:
        A, L, S, R = customers[customer_id - 1]
        service_order.append(customer_id)

        print(f"\nGoing to customer {customer_id}: A={A}, L={L}, S={S}, R={R}")
        print(f"Repairman at location {location}, time {time}")

        # Travel
        travel_time = abs(location - L)
        time += travel_time
        print(f"➡ Travel to L={L}: +{travel_time}, time = {time}")
        location = L

        # If arrived after customer's available time A, skip
        if time > A:
            print(f"❌ Customer {customer_id} missed (arrival {time} > available {A}), skipping.")
            continue

        # Wait if early (arrived before customer's available time A)
        if time < A:
            wait_time = A - time
            time = A
            print(f"⏳ Waiting for customer: +{wait_time}, time = {time}")

        # Repair
        time += S
        print(f"🛠 Repairing: +{S}, time = {time}")

        # Return
        time += R
        location = 0
        print(f"🏠 Returning: +{R}, time = {time}")

    print("\n=== TRACE END ===")
    print("\nFinal Order:", *service_order)
    print("Final Time:", time)

repair_service_trace()