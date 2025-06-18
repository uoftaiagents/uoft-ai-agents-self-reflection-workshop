"""
Simple Self-Reflecting AI Agents Library
========================================

This module contains clean, educational implementations of self-reflecting AI agents.
All classes are self-contained with minimal dependencies for easy learning.
"""

import random
import time
from typing import Dict, List, Optional


class AISimulator:
    """
    Simulates realistic AI responses without requiring API keys.
    This replaces expensive API calls while teaching core concepts.
    """
    
    def __init__(self):
        # Comprehensive knowledge base for domain-specific responses
        self.knowledge = {
            "algorithms": {
                "keywords": ["recursive", "sorting", "complexity", "optimization", "algorithm", "binary search", "dynamic programming"],
                "responses": [
                    "For recursive algorithms, implement memoization to cache results and avoid redundant calculations. Consider the base case carefully and ensure stack overflow protection for deep recursions.",
                    "When optimizing sorting algorithms, consider the input characteristics: quicksort for general cases, mergesort for stability, radix sort for integers, and heapsort for guaranteed O(n log n).",
                    "Dynamic programming works best when you have overlapping subproblems and optimal substructure. Break the problem into smaller subproblems and build up the solution.",
                    "Profile your algorithm with realistic data sizes. Use Big O analysis but also measure real performance. Consider space-time tradeoffs and the specific constraints of your use case."
                ]
            },
            "systems": {
                "keywords": ["scalable", "architecture", "concurrent", "distributed", "system design", "microservices", "database"],
                "responses": [
                    "Design for horizontal scalability from the start. Use load balancers, implement caching layers (Redis/Memcached), and consider database sharding strategies.",
                    "In distributed systems, understand CAP theorem trade-offs. Choose between consistency and availability based on your use case. Implement proper circuit breakers and retry mechanisms.",
                    "For concurrent systems, use thread-safe data structures, minimize shared state, and consider message-passing over shared memory. Always handle race conditions and deadlocks.",
                    "Monitor system health with comprehensive metrics (latency, throughput, error rates). Implement distributed tracing and establish clear SLA targets."
                ]
            },
            "machine_learning": {
                "keywords": ["machine learning", "ml", "overfitting", "model", "training", "data", "neural network", "gradient descent", "learn machine learning", "ai", "artificial intelligence", "classification", "regression", "clustering", "supervised", "unsupervised", "dataset", "features", "algorithms", "unbalanced", "imbalanced", "bias", "variance", "cross-validation", "hyperparameters", "deep learning", "preprocessing"],
                "responses": [
                    "For unbalanced classification problems, use techniques like SMOTE for oversampling, undersampling majority class, or cost-sensitive learning. Evaluate with precision, recall, F1-score, and AUC-ROC rather than just accuracy.",
                    "Prevent overfitting through regularization (L1/L2), dropout, early stopping, and cross-validation. Use more training data when possible and consider ensemble methods to reduce variance.",
                    "Start with simple algorithms (logistic regression, decision trees) before complex ones. Focus on feature engineering and data quality - clean, relevant features often matter more than complex models.",
                    "For classification problems, understand your evaluation metrics: accuracy for balanced datasets, precision/recall for imbalanced ones, and AUC-ROC for ranking problems. Always use proper train/validation/test splits."
                ]
            },
            "debugging": {
                "keywords": ["debug", "debugging", "error", "bug", "crash", "exception", "troubleshoot"],
                "responses": [
                    "Use systematic debugging: reproduce the issue consistently, check logs and error messages, use debugger breakpoints, and isolate the problem to the smallest failing case.",
                    "For production debugging, implement comprehensive logging with different levels (DEBUG, INFO, WARN, ERROR). Use distributed tracing in microservices to track request flows.",
                    "Common debugging strategies: rubber duck debugging, binary search through code changes, checking recent modifications, and validating assumptions with assertions.",
                    "Performance debugging requires profiling tools. Identify bottlenecks with CPU and memory profilers, database query analyzers, and network monitoring tools."
                ]
            },
            "web_development": {
                "keywords": ["web", "frontend", "backend", "api", "javascript", "react", "node", "performance"],
                "responses": [
                    "For frontend performance, optimize bundle sizes with code splitting, lazy loading, and tree shaking. Minimize DOM manipulations and use virtual DOM efficiently.",
                    "API design should follow RESTful principles or GraphQL best practices. Implement proper error handling, rate limiting, and authentication/authorization.",
                    "Backend optimization involves database query optimization, caching strategies, connection pooling, and efficient data serialization (JSON vs Protocol Buffers).",
                    "Modern web apps need responsive design, accessibility (WCAG guidelines), progressive enhancement, and cross-browser compatibility testing."
                ]
            },
            "data_structures": {
                "keywords": ["data structure", "array", "linked list", "tree", "graph", "hash table", "queue", "stack"],
                "responses": [
                    "Choose data structures based on operations: arrays for random access, linked lists for frequent insertions/deletions, hash tables for O(1) lookups.",
                    "For tree structures, consider balance: use AVL or Red-Black trees for guaranteed O(log n) operations, or B-trees for disk-based storage systems.",
                    "Graph algorithms require careful choice of representation: adjacency lists for sparse graphs, adjacency matrices for dense graphs. Consider directed vs undirected.",
                    "Advanced structures like segment trees, tries, and disjoint sets solve specific problems efficiently. Understand the problem pattern before choosing."
                ]
            },
            "security": {
                "keywords": ["security", "authentication", "encryption", "vulnerability", "attack", "secure"],
                "responses": [
                    "Implement defense in depth: input validation, output encoding, authentication, authorization, encryption in transit and at rest, and security monitoring.",
                    "For web security, protect against OWASP Top 10: SQL injection, XSS, CSRF, insecure direct object references, and security misconfigurations.",
                    "Use established cryptographic libraries, never roll your own crypto. Implement proper key management, use strong random number generators, and keep dependencies updated.",
                    "Security testing should include static analysis, dynamic testing, dependency scanning, and penetration testing. Regular security audits are essential."
                ]
            },
            "career": {
                "keywords": ["career", "job", "interview", "internship", "resume", "portfolio", "networking"],
                "responses": [
                    "Build a strong portfolio with 3-5 diverse projects showcasing different skills. Include clean code, documentation, and deployed demos when possible.",
                    "For technical interviews, practice coding problems daily, understand system design basics, and prepare behavioral stories using the STAR method.",
                    "Network actively through tech meetups, LinkedIn, GitHub contributions, and informational interviews. Quality connections matter more than quantity.",
                    "Tailor your resume for each application, highlighting relevant projects and skills. Keep it concise, quantify achievements, and proofread carefully."
                ]
            },
            "programming": {
                "keywords": ["programming", "coding", "software development", "best practices", "clean code"],
                "responses": [
                    "Write clean, readable code with meaningful variable names, consistent formatting, and clear comments. Follow SOLID principles and design patterns.",
                    "Practice version control with Git, write comprehensive tests, and use continuous integration. Code review and pair programming improve quality.",
                    "Learn multiple programming paradigms: object-oriented, functional, and procedural. Master one language deeply before learning others.",
                    "Focus on problem-solving skills over syntax memorization. Break complex problems into smaller pieces and test iteratively."
                ]
            },
            "learning": {
                "keywords": ["learn", "study", "education", "skills", "improvement", "development"],
                "responses": [
                    "Use active learning: build projects, teach others, and practice spaced repetition. Theory + hands-on practice is most effective.",
                    "Set specific, measurable goals with deadlines. Track progress and adjust methods based on what works for your learning style.",
                    "Join communities, find mentors, and engage with peers. Learning is social - discussion and collaboration accelerate understanding.",
                    "Focus on fundamentals first, then specialize. Solid foundations in math, CS theory, and problem-solving transfer across domains."
                ]
            }
        }
    
    def generate_response(self, prompt: str, style: str = "balanced") -> str:
        """Generate a response based on prompt content and style."""
        prompt_lower = prompt.lower()
        
        # Determine domain with improved matching logic
        domain = "general"
        best_match_score = 0
        
        for d, info in self.knowledge.items():
            # Count keyword matches
            match_count = sum(1 for keyword in info["keywords"] if keyword in prompt_lower)
            
            # Calculate match score with priority weighting
            match_score = match_count
            
            # Give priority to domain-specific action words (debugging, learning, etc.)
            priority_keywords = {
                "debugging": ["debug", "debugging", "troubleshoot", "error", "bug"],
                "machine_learning": ["learn machine learning", "ml", "ai", "artificial intelligence"],
                "systems": ["design", "architecture", "scalable", "distributed"],
                "algorithms": ["algorithm", "complexity", "sorting", "optimization"],
                "web_development": ["web", "frontend", "backend", "api"],
                "security": ["security", "authentication", "encryption"],
                "career": ["career", "job", "interview", "internship"],
                "programming": ["programming", "coding", "software development"],
                "learning": ["learn", "study", "education", "skills"]
            }
            
            # Boost score for priority keywords that appear in the prompt
            if d in priority_keywords:
                for priority_keyword in priority_keywords[d]:
                    if priority_keyword in prompt_lower:
                        match_score += 0.5  # Boost for priority keywords
            
            if match_score > best_match_score:
                best_match_score = match_score
                domain = d
        
        # Generate base response based on domain
        if domain in self.knowledge and best_match_score > 0:
            base_response = random.choice(self.knowledge[domain]["responses"])
        else:
            base_response = "Analyze the problem systematically by breaking it into smaller components, researching existing solutions, and implementing a well-tested approach."
        
        # Apply style-specific modifications - make them substantially different
        if style == "technical":
            if domain == "algorithms":
                technical_addon = " Focus on computational complexity analysis, memory usage patterns, and implementation-specific optimizations like cache locality and branch prediction."
            elif domain == "machine_learning":
                technical_addon = " Dive into mathematical foundations, gradient computations, loss function analysis, and hyperparameter optimization strategies."
            elif domain == "systems":
                technical_addon = " Consider low-level implementation details, system calls, memory management, and hardware-specific optimizations."
            else:
                technical_addon = " Examine implementation details, performance characteristics, and technical constraints thoroughly."
            
            return f"Technical Analysis: {base_response}{technical_addon}"
            
        elif style == "creative":
            if domain == "algorithms":
                creative_addon = " Think beyond standard approaches - consider unconventional data structures, hybrid algorithms, or bio-inspired computing methods."
            elif domain == "machine_learning":
                creative_addon = " Explore novel architectures, transfer learning from unexpected domains, or ensemble methods combining different paradigms."
            elif domain == "systems":
                creative_addon = " Consider unconventional architectures, event-driven designs, or innovative caching patterns from other industries."
            else:
                creative_addon = " Challenge conventional wisdom and explore innovative approaches from adjacent fields or emerging technologies."
            
            return f"Creative Approach: {base_response}{creative_addon}"
            
        elif style == "systematic":
            steps = [
                "1) Problem Analysis: Break down requirements and constraints",
                "2) Solution Design: " + base_response,
                "3) Implementation: Build incrementally with continuous testing",
                "4) Validation: Verify correctness and performance against requirements"
            ]
            return "Systematic Methodology:\n" + "\n".join(steps)
        
        else:  # balanced
            # Return balanced response without delay for better workshop experience
            return f"Balanced Solution: {base_response} Consider both immediate implementation needs and long-term maintainability."
    
    def critique_response(self, response: str, mode: str = "constructive") -> List[str]:
        """Provide critique of a response based on evaluation mode."""
        critiques = []
        
        # Basic quality checks
        if len(response) < 100:
            critiques.append("Response needs more depth and detailed explanation")
        
        if len(response) > 500:
            critiques.append("Response might be too verbose - consider making it more concise")
        
        # Content quality checks
        if not any(word in response.lower() for word in ["step", "approach", "consider", "implement", "strategy", "method"]):
            critiques.append("Missing clear methodology or actionable approach")
        
        if response.count('.') < 2:
            critiques.append("Should include multiple points or considerations")
        
        # Domain-specific critiques
        response_lower = response.lower()
        if any(word in response_lower for word in ["algorithm", "complexity", "optimization"]):
            if not any(word in response_lower for word in ["o(", "time", "space", "performance", "complexity"]):
                critiques.append("Algorithm discussions should address complexity analysis")
        
        if any(word in response_lower for word in ["machine learning", "model", "training"]):
            if not any(word in response_lower for word in ["data", "validation", "overfitting", "accuracy", "metrics"]):
                critiques.append("ML discussions should address data quality and model validation")
        
        if any(word in response_lower for word in ["system", "scalable", "distributed"]):
            if not any(word in response_lower for word in ["scalability", "performance", "monitoring", "availability"]):
                critiques.append("System design should consider scalability and reliability")
        
        # Mode-specific critiques
        if mode == "critical":
            if "trade-off" not in response_lower and "tradeoff" not in response_lower:
                critiques.append("Should explicitly discuss trade-offs and limitations")
            
            if not any(word in response_lower for word in ["risk", "challenge", "limitation", "constraint", "drawback"]):
                critiques.append("Should acknowledge potential challenges or limitations")
            
            if "example" not in response_lower and "e.g." not in response_lower:
                critiques.append("Could strengthen with concrete examples or use cases")
        
        elif mode == "constructive":
            if "best practice" not in response_lower and "recommended" not in response_lower:
                critiques.append("Could include industry best practices or recommendations")
            
            if len([s for s in response.split('.') if len(s.strip()) > 20]) < 3:
                critiques.append("Could expand with more detailed explanations")
            
            if not any(word in response_lower for word in ["testing", "validation", "verification", "quality"]):
                critiques.append("Should mention testing or quality assurance aspects")
        
        return critiques if critiques else ["Response meets quality standards"]


class SimpleReflectiveAgent:
    """
    A self-reflecting agent that can generate, critique, and refine its responses.
    Perfect for educational purposes with clear, understandable logic.
    """
    
    def __init__(self, ai_simulator: Optional[AISimulator] = None):
        self.ai = ai_simulator or AISimulator()
        self.trace = []  # Keep track of the reflection process
    
    def solve(self, problem: str, max_iterations: int = 3, style: str = "balanced", 
              critique_mode: str = "constructive", verbose: bool = True) -> str:
        """
        Solve a problem using self-reflection.
        
        Args:
            problem: The problem to solve
            max_iterations: Maximum number of refinement iterations
            style: Generation style ("technical", "creative", "systematic", "balanced")
            critique_mode: Evaluation mode ("critical", "constructive", "comprehensive")
            verbose: If True, print progress; if False, suppress output
        """
        if verbose:
            print(f"🔍 Problem: {problem}")
            print(f"⚙️ Style: {style} | Critique: {critique_mode}")
            print("-" * 60)
        # Generate initial response
        response = self.ai.generate_response(problem, style)
        self.trace = [{"iteration": 0, "response": response, "critiques": []}]
        for i in range(max_iterations):
            if verbose:
                print(f"\n🔄 Iteration {i+1}")
                print(f"💡 Current response: {response}")
            critiques = self.ai.critique_response(response, critique_mode)
            if verbose:
                print(f"🔍 Critiques: {', '.join(critiques)}")
            if critiques == ["Response meets quality standards"]:
                if verbose:
                    print("✅ Response satisfactory!")
                break
            refined_response = self._refine_response(response, critiques)
            if verbose:
                print(f"✨ Refined: {refined_response[:100]}...")
            response = refined_response
            self.trace.append({
                "iteration": i+1, 
                "response": response, 
                "critiques": critiques
            })
        if verbose:
            print(f"\n🎯 Final response after {len(self.trace)} iterations:")
            print("📋 COMPLETE FINAL RESULT:")
            print(response)
            print("-" * 60)
        return response
    
    def _refine_response(self, response: str, critiques: List[str]) -> str:
        """Refine response based on critiques."""
        refined = response
        
        for critique in critiques:
            critique_lower = critique.lower()
            
            # Basic quality improvements
            if "needs more depth" in critique_lower or "detailed explanation" in critique_lower:
                refined += " This approach should be implemented with careful consideration of edge cases, error handling, and performance implications in production environments."
            
            elif "too verbose" in critique_lower:
                # Simplify by removing redundant phrases
                sentences = refined.split('.')
                refined = '. '.join(sentences[:3]) + '.' if len(sentences) > 3 else refined
            
            elif "missing clear methodology" in critique_lower:
                refined = f"Methodology: {refined} This systematic approach ensures comprehensive problem-solving."
            
            elif "multiple points" in critique_lower:
                refined += " Additionally, consider documentation, code review processes, and maintenance strategies."
            
            # Domain-specific improvements
            elif "complexity analysis" in critique_lower:
                refined += " Performance Analysis: Evaluate time complexity (worst, average, best case) and space complexity. Consider optimization opportunities and scalability limits."
            
            elif "model validation" in critique_lower:
                refined += " ML Best Practices: Implement proper train/validation/test splits, use cross-validation, monitor for data drift, and establish baseline metrics."
            
            elif "scalability and reliability" in critique_lower:
                refined += " System Design: Plan for horizontal scaling, implement health checks, design for failure resilience, and establish monitoring/alerting."
            
            # Critical mode improvements
            elif "trade-offs and limitations" in critique_lower:
                refined += " Trade-offs: Consider performance vs. complexity, development time vs. optimization, and cost vs. reliability implications."
            
            elif "potential challenges" in critique_lower:
                refined += " Challenges: Be aware of implementation complexity, resource requirements, and potential failure modes."
            
            elif "concrete examples" in critique_lower:
                refined += " Example: In practice, this might involve specific tools like profilers for performance optimization or A/B testing for feature validation."
            
            # Constructive mode improvements
            elif "best practices" in critique_lower:
                refined += " Best Practices: Follow industry standards, use established patterns, and leverage proven frameworks when possible."
            
            elif "more detailed explanations" in critique_lower:
                refined += " This ensures maintainable, scalable solutions that can evolve with changing requirements."
            
            elif "testing or quality assurance" in critique_lower:
                refined += " Quality Assurance: Implement comprehensive testing (unit, integration, end-to-end), code reviews, and continuous integration practices."
        
        return refined
    
    def get_trace(self) -> List[Dict]:
        """Get the full trace of the reflection process."""
        return self.trace
    
    def print_analysis(self):
        """Print analysis of the reflection process."""
        if not self.trace:
            print("No reflection trace available.")
            return
        
        print("\n📊 Reflection Analysis:")
        print(f"• Total iterations: {len(self.trace)}")
        
        lengths = [len(item["response"]) for item in self.trace]
        print(f"• Response length progression: {lengths}")
        print(f"• Average improvement per iteration: {(lengths[-1] - lengths[0]) / len(lengths):.1f} characters")
        
        critique_counts = [len(item["critiques"]) for item in self.trace if item["critiques"]]
        if critique_counts:
            print(f"• Critique counts: {critique_counts}")
            print(f"• Quality improved: {'Yes' if critique_counts and critique_counts[-1] < critique_counts[0] else 'Maintained'}")


class AdvancedReflectiveAgent(SimpleReflectiveAgent):
    """
    Extended version with multiple strategies and evaluation modes.
    Builds on the simple agent with more sophisticated capabilities.
    """
    
    def __init__(self, ai_simulator: Optional[AISimulator] = None):
        super().__init__(ai_simulator)
        self.strategies = {
            'technical': self._technical_generate,
            'creative': self._creative_generate,
            'systematic': self._systematic_generate
        }
        self.evaluation_modes = {
            'critical': self._critical_evaluate,
            'constructive': self._constructive_evaluate,
            'comprehensive': self._comprehensive_evaluate
        }
    
    def _technical_generate(self, problem: str) -> str:
        """Generate technical, implementation-focused responses."""
        base = self.ai.generate_response(problem, "technical")
        
        # Add technical depth based on problem domain
        problem_lower = problem.lower()
        if any(word in problem_lower for word in ['recursive', 'algorithm', 'complexity']):
            technical_detail = " Implementation Details: Consider stack overflow protection, tail recursion optimization, and iterative alternatives. Profile memory usage and CPU cycles."
        elif any(word in problem_lower for word in ['machine learning', 'model', 'neural']):
            technical_detail = " Technical Specifics: Analyze gradient flow, implement proper weight initialization, consider batch normalization, and optimize computational graphs."
        elif any(word in problem_lower for word in ['system', 'database', 'distributed']):
            technical_detail = " System Architecture: Design for ACID properties, implement connection pooling, consider sharding strategies, and plan for eventual consistency."
        else:
            technical_detail = " Technical Implementation: Focus on code efficiency, memory management, error handling, and performance profiling."
        
        return base + technical_detail
    
    def _creative_generate(self, problem: str) -> str:
        """Generate creative, innovative responses."""
        base = self.ai.generate_response(problem, "creative")
        
        # Add creative insights based on domain
        problem_lower = problem.lower()
        if any(word in problem_lower for word in ['algorithm', 'optimization']):
            creative_insight = " Innovation Opportunity: Consider bio-inspired algorithms, quantum computing approaches, or machine learning-assisted optimization."
        elif any(word in problem_lower for word in ['machine learning', 'ai']):
            creative_insight = " Creative ML: Explore meta-learning, few-shot learning, or novel attention mechanisms from different domains."
        elif any(word in problem_lower for word in ['system', 'architecture']):
            creative_insight = " Architectural Innovation: Consider event sourcing, CQRS patterns, or blockchain-inspired distributed consensus mechanisms."
        else:
            creative_insight = " Creative Thinking: Draw inspiration from nature, other industries, or emerging technologies."
        
        return base + creative_insight
    
    def _systematic_generate(self, problem: str) -> str:
        """Generate methodical, structured responses."""
        base = self.ai.generate_response(problem, "systematic")
        
        # Add systematic framework
        systematic_framework = """
        **Phase 1: Analysis** - Requirements gathering, constraint identification, stakeholder needs
        **Phase 2: Design** - Architecture planning, component specification, interface definition
        **Phase 3: Implementation** - Incremental development, continuous testing, code review
        **Phase 4: Validation** - Performance testing, user acceptance, deployment verification
        **Phase 5: Maintenance** - Monitoring, optimization, iterative improvement"""
        
        return base + systematic_framework
    
    def _critical_evaluate(self, response: str) -> List[str]:
        """Critical evaluation focusing on flaws and weaknesses."""
        critiques = self.ai.critique_response(response, "critical")
        
        # Add domain-specific critical analysis
        additional_critiques = []
        if len(response) < 100:
            additional_critiques.append("Response lacks comprehensive analysis")
        if '?' in response:
            additional_critiques.append("Should provide definitive guidance rather than questions")
        
        return critiques + additional_critiques
    
    def _constructive_evaluate(self, response: str) -> List[str]:
        """Constructive evaluation suggesting improvements."""
        return self.ai.critique_response(response, "constructive")
    
    def _comprehensive_evaluate(self, response: str) -> List[str]:
        """Comprehensive evaluation covering multiple aspects."""
        critical = self._critical_evaluate(response)
        constructive = self._constructive_evaluate(response)
        return list(set(critical + constructive))  # Remove duplicates
    
    def solve(self, problem: str, generation_strategy: str = 'technical', 
              evaluation_mode: str = 'critical', max_iterations: int = 3, verbose: bool = True) -> str:
        """
        Advanced solving with configurable strategies.
        
        Args:
            problem: Problem to solve
            generation_strategy: 'technical', 'creative', or 'systematic'
            evaluation_mode: 'critical', 'constructive', or 'comprehensive'
            max_iterations: Maximum refinement iterations
            verbose: If True, print progress; if False, suppress output
        """
        if verbose:
            print(f"🔬 Problem: {problem}")
            print(f"⚙️ Strategy: {generation_strategy} | Evaluation: {evaluation_mode}")
        if generation_strategy in self.strategies:
            response = self.strategies[generation_strategy](problem)
        else:
            response = self.ai.generate_response(problem)
        self.trace = [{"iteration": 0, "response": response, "critiques": []}]
        for i in range(max_iterations):
            if verbose:
                print(f"\n🔄 Iteration {i+1}")
                print(f"💡 Response: {response[:100]}...")
            if evaluation_mode in self.evaluation_modes:
                critiques = self.evaluation_modes[evaluation_mode](response)
            else:
                critiques = self.ai.critique_response(response)
            if verbose:
                print(f"🔍 Critique: {critiques[0] if critiques else 'No issues found'}")
            if not critiques or 'meets quality standards' in str(critiques):
                if verbose:
                    print("✅ Response satisfactory!")
                break
            response = self._refine_response(response, critiques)
            self.trace.append({
                "iteration": i+1,
                "response": response, 
                "critiques": critiques
            })
        if verbose:
            print(f"\n🎯 Final response after {len(self.trace)} iterations:")
            print("📋 COMPLETE FINAL RESULT:")
            print(response)
            print("-" * 60)
        return response


def calculate_metrics(response: str) -> Dict:
    """Calculate basic metrics for response analysis."""
    if not response:
        return {"length": 0, "words": 0, "sentences": 0, "complexity_score": 0}
    
    return {
        "length": len(response),
        "words": len(response.split()),
        "sentences": response.count('.') + response.count('!') + response.count('?'),
        "complexity_score": len([w for w in response.split() if len(w) > 6]) / len(response.split()) if response.split() else 0
    }


# Convenience function for quick experimentation
def quick_reflect(problem: str, style: str = "balanced", iterations: int = 2) -> str:
    """Quick reflection for experimentation."""
    agent = SimpleReflectiveAgent()
    return agent.solve(problem, max_iterations=iterations, style=style)


if __name__ == "__main__":
    # Quick test
    print("🧪 Testing Simple Reflective Agent...")
    result = quick_reflect("How do I optimize a recursive algorithm?", "technical", 2)
    print(f"\n🎯 Result: {result}")
