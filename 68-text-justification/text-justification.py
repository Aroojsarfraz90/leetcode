class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            line_words = []
            line_length = 0

            # Ek line mein maximum words add karo
            while i < len(words):
                # len(line_words) minimum spaces ko represent karta hai
                if line_length + len(words[i]) + len(line_words) <= maxWidth:
                    line_words.append(words[i])
                    line_length += len(words[i])
                    i += 1
                else:
                    break

            # Last line: left justified
            if i == len(words):
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)

            # Sirf ek word wali line
            elif len(line_words) == 1:
                line = line_words[0]
                line += " " * (maxWidth - len(line))
                result.append(line)

            # Normal line: fully justified
            else:
                total_spaces = maxWidth - line_length
                gaps = len(line_words) - 1

                even_spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""

                for j in range(gaps):
                    line += line_words[j]

                    # Extra spaces left-side gaps ko milengi
                    spaces = even_spaces

                    if j < extra_spaces:
                        spaces += 1

                    line += " " * spaces

                line += line_words[-1]
                result.append(line)

        return result