from calculator import estimate_band_size

def main():
    print("Gel Band Size Calculator")

    ladder_sizes = list(map(float, input("Ladder sizes: ").split(",")))
    ladder_distances = list(map(float, input("Ladder distances: ").split(",")))
    sample_distance = float(input("Sample distance: "))

    result = estimate_band_size(ladder_sizes, ladder_distances, sample_distance)
    print(f"Estimated size: {result:.2f} bp")

if __name__ == "__main__":
    main()
